import streamlit as st
from datetime import datetime
from llm_utils import cover_letter_prompt, job_analysis_prompt
import os
from groq import Groq
from config.styles import apply_custom_styles, set_page_config, header_section
from pdf_utils import extract_text_from_pdf, create_cover_letter_pdf
from dotenv import load_dotenv
load_dotenv()


# Configure APIs

# configure Groq
api_key = None
try:
    if 'GROQ_API_KEY' in st.secrets:
        api_key = st.secrets['GROQ_API_KEY']
except Exception:
    pass

if not api_key and 'GROQ_API_KEY' in os.environ:
    api_key = os.environ['GROQ_API_KEY']
if not api_key:
    raise ValueError("GROQ_API_KEY not found in Streamlit secrets or environment variables.")

GROQ_CLIENT = Groq(api_key=api_key)

# Models
groq_model = "meta-llama/llama-4-scout-17b-16e-instruct"
#groq_model = "openai/gpt-oss-120b"

# Initialize session state
def init_session_state():
    defaults = {
        'cover_letter': "",
        'cover_letter_fr': "",
        'show_french': False,
        'job_analysis': "",
        'uploaded_resume': "",
        'execution_time': None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value



def translate_to_french(text):
    """Translate text to French using Groq"""
    try:
        response = GROQ_CLIENT.chat.completions.create(
            messages=[{
                "role": "user", 
                "content": f"Translate this professional text to French. Maintain the professional tone and formatting:\n\n{text}"
            }],
            model=groq_model
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Translation error: {str(e)}")
        return None

def update_cover_letter_state():
    """Update cover letter state when text area is edited"""
    if st.session_state.show_french:
        # Update French version
        if f"cover_letter_display_fr" in st.session_state:
            st.session_state.cover_letter_fr = st.session_state.cover_letter_display_fr
    else:
        # Update English version
        if f"cover_letter_display_en" in st.session_state:
            st.session_state.cover_letter = st.session_state.cover_letter_display_en

def main():
    # Initialize
    init_session_state()
    
    # Set page config
    apply_custom_styles()
    set_page_config ()
    header_section()
    
    st.divider()

    # Main layout
    col1, col2 = st.columns([1.2, 1])

    with col1:
        # PDF Upload Section
        st.markdown("### 📄 Upload Your CV (PDF)")
        uploaded_file = st.file_uploader(
            "Upload your CV/Resume",
            type=["pdf"],
            help="Upload your CV in PDF format for text extraction"
        )

        if uploaded_file is not None:
            try:
                st.session_state.uploaded_resume = extract_text_from_pdf(uploaded_file)
                st.success(f"✅ CV uploaded: {uploaded_file.name}")
            except Exception as e:
                st.error(f"❌ Error reading PDF: {str(e)}")

        st.markdown("### 📋 Job Description")
        job_description = st.text_area(
            "Paste the complete job description:",
            height=300,
            placeholder="Paste the complete job description including requirements and company information...",
            help="Include all relevant details for better customization"
        )
        
        # Action buttons
        col_btn1, col_btn2 = st.columns(2)
        st.divider()

        with col_btn1:
            if st.button("🔍 Analyze Job", type="secondary", use_container_width=True):
                if not job_description.strip():
                    st.warning("⚠️ Please enter a job description first.")
                else:
                    with st.spinner("🔄 Analyzing job description..."):
                        try:
                            start_time = datetime.now()
                            response = GROQ_CLIENT.chat.completions.create(
                                messages=[{"role": "user", "content": job_analysis_prompt(job_description)}],
                                model=groq_model
                            )
                            st.session_state.job_analysis = response.choices[0].message.content
                            st.session_state.execution_time = datetime.now() - start_time
                            st.success("✅ Job analysis completed!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"❌ Error: {str(e)}")

        with col_btn2:
            if st.button("✨ Generate Cover Letter", type="primary", use_container_width=True):
                if not job_description.strip():
                    st.warning("⚠️ Please enter a job description first.")
                elif not st.session_state.uploaded_resume:
                    st.error("❌ Please upload your CV first.")
                else:
                    with st.spinner("🔄 Generating your personalized cover letter..."):
                        try:
                            start_time = datetime.now()
                            response = GROQ_CLIENT.chat.completions.create(
                                messages=[{"role": "user", "content": cover_letter_prompt(job_description, st.session_state.uploaded_resume)}],
                                model=groq_model
                            )
                            st.session_state.cover_letter = response.choices[0].message.content
                            st.session_state.cover_letter_fr = ""  # Reset French version
                            st.session_state.execution_time = datetime.now() - start_time
                            st.session_state.show_french = False  # Reset French view
                            st.success("✅ Cover letter generated successfully!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"❌ Error: {str(e)}")
        
        # Job Analysis Display
        if st.session_state.job_analysis:
            st.markdown("### 📊 Job Analysis")
                # st.text_area(
                #     "Job Analysis Results:",
                #     value=st.session_state.job_analysis,
                #     height=500,
                #     key="job_analysis_display"
                # )
                
            st.success(st.session_state.job_analysis)
            
            # Download job analysis
            st.download_button(
                label="📄 Download Analysis",
                data=st.session_state.job_analysis,
                file_name=f"job_analysis_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain",
                use_container_width=True
            )
    
    with col2:
        st.markdown("### 📝 Cover Letter")

        if st.session_state.cover_letter:
            # Language toggle buttons
            col_en, col_fr = st.columns(2)
            with col_en:
                if st.button("🇺🇸 English", use_container_width=True, type="primary" if not st.session_state.show_french else "secondary"):
                    st.session_state.show_french = False
                    st.rerun()

            with col_fr:
                if st.button("🇫🇷 Français", use_container_width=True, type="primary" if st.session_state.show_french else "secondary"):
                    # Always translate based on current English content
                    with st.spinner("🔄 Translating to French..."):
                        current_english = st.session_state.get("cover_letter_display_en", st.session_state.cover_letter)
                        st.session_state.cover_letter_fr = translate_to_french(current_english)
                    st.session_state.show_french = True
                    st.rerun()

            # Display appropriate version
            current_letter = st.session_state.cover_letter_fr if st.session_state.show_french and st.session_state.cover_letter_fr else st.session_state.cover_letter
            language_suffix = "_fr" if st.session_state.show_french else "_en"

            st.text_area(
                f"Your cover letter ({'French' if st.session_state.show_french else 'English'}):",
                value=current_letter,
                height=400,
                key=f"cover_letter_display{language_suffix}",
                on_change=lambda: update_cover_letter_state()
            )
            st.caption("You can edit the text above before downloading")

            # PDF Download buttons - always show both
            st.markdown("#### 📥 Download as PDF")
            col_pdf_en, col_pdf_fr = st.columns(2)

            with col_pdf_en:
                english_letter = st.session_state.get("cover_letter_display_en", st.session_state.cover_letter)
                if english_letter:
                    try:
                        pdf_en = create_cover_letter_pdf(english_letter, "Jithin_Raj", "en")
                        st.download_button(
                            label="📥 English PDF",
                            data=pdf_en,
                            file_name=f"cover_letter_{datetime.now().strftime('%Y%m%d')}_en.pdf",
                            mime="application/pdf",
                            use_container_width=True
                        )
                    except Exception as e:
                        st.error(f"Error creating English PDF: {str(e)}")

            with col_pdf_fr:
                french_letter = st.session_state.get("cover_letter_display_fr", st.session_state.cover_letter_fr)
                if french_letter:
                    try:
                        pdf_fr = create_cover_letter_pdf(french_letter, "Jithin_Raj", "fr")
                        st.download_button(
                            label="📥 French PDF",
                            data=pdf_fr,
                            file_name=f"cover_letter_{datetime.now().strftime('%Y%m%d')}_fr.pdf",
                            mime="application/pdf",
                            use_container_width=True
                        )
                    except Exception as e:
                        st.error(f"Error creating French PDF: {str(e)}")
                else:
                    st.info("🇫🇷 Click 'Français' to generate French version")
        else:
            st.info("👆 Upload your CV and paste a job description, then click 'Generate Cover Letter'")
                   
    
    # Execution time display
    if st.session_state.execution_time:
        st.info(f"⏱️ Execution Time: {st.session_state.execution_time}")

if __name__ == "__main__":
    main()