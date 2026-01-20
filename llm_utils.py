# def cover_letter_prompt(job_description: str, resume: str) -> str:
    
#     """Generate a cover letter prompt based on job description and resume"""
    
#     return f"""
#     Create a professional cover letter for the following job position using my resume. Follow this template exactly:

#     Jithin Raj Reghuvaran
#     Recent Master 2 Graduate in Data Science from France
#     Paris, France
#     (+33) 745293669 | [jithinrajr98@gmail.com](mailto:jithinrajr98@gmail.com)

#     Subject: Application for the position of [JOB TITLE]

#     Dear Hiring Manager,

#     I'm writing to express my strong interest in the [JOB TITLE] position at [COMPANY NAME]. I am recent Master 2 graduate in Data Science from France with [X] years of experience in [KEY SKILL AREA 1] and [KEY SKILL AREA 2]. I've successfully delivered results such as [SPECIFIC ACHIEVEMENT OR PROJECT TYPE].

#     My expertise with [RELEVANT TOOL/TECHNOLOGY 1], and [RELEVANT TOOL/TECHNOLOGY 2], aligns well with your requirements. For example, I [QUANTIFIED ACHIEVEMENT] by [SPECIFIC ACTION], resulting in [MEASURABLE OUTCOME].

#     I'm particularly drawn to [COMPANY NAME] because of [SPECIFIC COMPANY PROJECT/INITIATIVE OR VALUES]. My experience in [KEY EXPERTISE AREA] would enable me to contribute meaningfully to [SPECIFIC TEAM GOAL OR CHALLENGE].

#     I would welcome the opportunity to discuss how my background in [RELEVANT FIELD] could support your team's objectives.

#     Best regards,
#     Jithin Raj Reghuvaran

#     **Guidelines:**
#     1. Keep the letter concise and professional (150-200 words max)
#     2. Focus on quantifiable achievements from my resume that relate to the job
#     3. Match at least 3 key requirements from the job description
#     4. If the job description doesn't match my resume perfectly, write a brief but enthusiastic letter expressing genuine interest
#     5. Extract the company name and job title from the job description
#     6. Use specific examples and metrics where possible
#     7. Maintain a confident but humble tone
#     8. Highlight the Master 2 Data Science degree when relevant to the position

#     **Job Description:**
#     {job_description}

#     **My Resume:**
#     {resume}

#     Generate ONLY the cover letter text, no additional commentary.
#     """

def cover_letter_prompt(job_description: str, resume: str) -> str:
    """Generate a concise, direct cover letter prompt with dynamic content based on job requirements"""

    return f"""
Create a concise, direct cover letter that dynamically adapts to job requirements. Position the candidate as a builder/engineer who SHIPS production systems.

Subject: Application for [JOB TITLE] Position at [COMPANY NAME]

Dear Hiring Team,

[PARAGRAPH 1 - Identity & Confidence (EXACTLY 2 sentences, FULLY DYNAMIC)]

Sentence 1: "I'm a [ROLE from job title] with 5+ years of experience."
- Extract role from job title (e.g., "AI engineer", "data engineer", "MLOps engineer", "backend engineer")

Sentence 2: "With cumulative experience in [3 DOMAINS matching job requirements], I am confident in my ability to [ACTION tied to job's primary responsibility]."
- Select 3 experience domains that MATCH the job requirements:
  - For Agentic AI roles: "software development, LLM systems, and AI automation"
  - For Data Engineering roles: "data pipeline development, cloud infrastructure, and analytics platforms"
  - For MLOps roles: "model deployment, CI/CD pipelines, and production ML systems"
  - For Backend roles: "API development, microservices, and cloud-native systems"
- Confidence statement must tie to the job's PRIMARY responsibility:
  - Agentic AI: "design, develop, and implement agentic solutions"
  - Data Engineering: "architect scalable data platforms"
  - MLOps: "build and maintain ML infrastructure at scale"
  - Backend: "design and build high-performance backend services"

[PARAGRAPH 2 - Projects (DYNAMIC SELECTION based on job requirements)]

Opening: "I've built and shipped several production systems that directly map to [COMPANY]'s job requirements."

Then select 2-3 projects that BEST MATCH the job requirements:

| If Job Requires | Select These Projects |
|-----------------|----------------------|
| Agentic AI / LLM | SDR agentic AI system, RAG systems |
| Real-time / low-latency | Voice AI system (100K req, 200ms latency) |
| Data Engineering | Fabric platform, dbt optimization, ERP integration |
| MLOps / CI/CD | Pipeline optimization, deployment automation |
| Cloud / Azure | Fabric platform, Azure deployments |

Format each project:
- "For instance, I [ACTION VERB] [WHAT WAS BUILT] using [TECH], achieving [OUTCOME with numbers]."
- Action verbs: designed, built, deployed, shipped, optimized, scaled
- Lead with the MOST RELEVANT project to this specific job

[PARAGRAPH 3 - Closing (EXACTLY 1 sentence)]

Single sentence: "I'm excited to discuss how I can contribute to [COMPANY]'s [TEAM/INITIATIVE from job posting] and look forward to exploring this opportunity further."

Best regards,
Jithin Raj Reghuvaran

(+33) 745293669 | jithinrajr98@gmail.com

**STRICT REQUIREMENTS:**
1. Maximum 200 words (excluding subject line and signature)
2. Use "Dear Hiring Team," (NOT "Dear Hiring Manager,")
3. Paragraph 1: EXACTLY 2 sentences
   - Sentence 1: Role (from job title) + years of experience
   - Sentence 2: 3 experience domains (matched to job) + confidence statement (tied to job's primary responsibility)
4. Paragraph 2: 2-3 projects DYNAMICALLY SELECTED based on job requirements
   - Each project must MAP to a specific job requirement
   - Lead with the MOST RELEVANT project
5. Paragraph 3: EXACTLY 1 sentence closing
6. Extract company name, job title, team/initiative from job description
7. Use action verbs: designed, built, deployed, shipped, optimized, scaled
8. Include at least 2 quantified outcomes (latency, scale, efficiency, cost)
9. BANNED phrases (NEVER use these):
   - "where I can leverage"
   - "I'm drawn to"
   - "I'm eager to"
   - "I'm impressed by"
   - "I'm comfortable with"
   - "I'm confident that my technical expertise"
   - "passion for innovation"
   - "ideal fit"
   - "I believe"
   - "I feel"
   - "Dear Hiring Manager"
10. Position as engineer/builder, not researcher
11. Do NOT mention Master's degree

**Job Description:**
{job_description}

**My Resume:**
{resume}

Generate ONLY the cover letter text in the exact format shown above, no additional commentary.
"""

def profile_modifier_prompt(job_description: str, current_profile: str) -> str:
    
    """Generate a prompt to modify the profile section based on job description"""
    
    return f"""
Adapt the professional summary to match the target job description while maintaining credibility and core achievements. Follow these specific rules:

**ADAPTATION RULES:**
1. **Role Alignment**: Use the exact job title from the description or closest equivalent
2. **Skills Matching**: Prioritize skills mentioned in the job requirements
3. **Industry Language**: Use terminology and keywords from the job posting
4. **Achievement Preservation**: Keep all quantified achievements (dollar amounts, percentages, years)
5. **Experience Level**: Adjust experience level appropriately:
   - For senior roles: Emphasize leadership and strategic impact
   - For mid-level roles: Focus on hands-on expertise and project delivery  
   - For junior roles: Highlight relevant education, internships, or projects

**STRUCTURE TO MAINTAIN:**
- [ROLE TITLE] with [X]+ years of experience in [DOMAIN/TECHNOLOGY]
- Expert in [3 key technologies/skills that match job requirements].

**CONSTRAINTS:**
- Keep the same professional tone and confidence level
- Maintain 2 sentences maximum
- Preserve any specific client types (Fortune 500, etc.) and dollar figures
- Don't fabricate experience or skills not implied in the original

**Job Description:**
{job_description}

**Current Profile:**
{current_profile}

Return ONLY the modified profile summary, no additional text or explanations.
"""

def translation_prompt(text: str, target_language: str = "French", content_type: str = "cover letter") -> str:
    """Generate a prompt for translating professional content"""
    if content_type == "profile":
        instruction = "Translate the following professional profile summary to {target_language}."
        additional_context = "This is a CV/resume profile section that should maintain its professional impact and technical terminology. Don't translate specific technical terms like machine learning, deep learning or position names."
    else:
        instruction = f"Translate the following professional {content_type} to {target_language}."
        additional_context = f"This is a professional {content_type} that should maintain formal business correspondence standards. Don't translate specific technical terms  like machine learning, deep learning  or position names."
    
    return f"""
{instruction}

**Requirements:**
1. Maintain the professional tone and formal structure
2. Use appropriate business language conventions for {target_language}
3. Keep the formatting and structure intact
4. Preserve technical terms and industry jargon appropriately
5. Adapt cultural nuances appropriately (e.g., "Dear Hiring Team," to "Madame, Monsieur," in French)
6. {additional_context}
7. For the closing paragraph, use this exact French pattern:
   - "I'm excited to discuss how I can contribute to [COMPANY]'s [INITIATIVE]" → "Je serais ravi de mettre mes compétences au service de [INITIATIVE] de [COMPANY]"
   - "and look forward to exploring this opportunity further" → "et d'échanger davantage sur cette opportunité"

**Text to translate:**
{text}

Provide ONLY the translated text, no additional commentary.
"""



def job_analysis_prompt(job_description: str) -> str:
    """Analyze job description to extract key information"""
    return f"""
Analyze the following job description and extract key information in the exact format specified below:

**COMPANY_NAME:** [Extract the company name - if not mentioned, write "Not specified"]

**POSITION:** [Extract the exact job title/position name]

**CANDIDATE_REQUIREMENTS:** [2 sentences maximum describing what the company is looking for in the ideal candidate - focus on experience, qualifications, and key attributes they want]

**TECHNICAL_SKILLS:** [2 sentences maximum listing the main technical skills, tools, programming languages, frameworks, or technologies required - be specific and include as many as mentioned]

**COMPANY_MISSION:** [1 sentence describing the company's mission, purpose, or what they do as a business - if not explicitly stated, infer from context]

**Instructions:**
- Extract information ONLY from the provided job description
- Use exact terminology and keywords from the job posting
- Be concise but comprehensive within the sentence limits
- If any information is completely missing from the job description, write "Not specified" for that section
- Focus on the most important and relevant details for each category
- Maintain professional language and avoid speculation beyond what's stated

**Job Description:**
{job_description}

Provide your analysis in the exact format above with the specified headings.
"""