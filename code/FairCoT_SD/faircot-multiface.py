# -*- coding: utf-8 -*-

import os




professions_prompts =  {

    "Doctor": [

        "Interfaith Representation in Medicine: A female doctor wearing a hijab, standing alongside a male doctor with a Sikh turban, and another male doctor wearing a Star of David necklace. They are in a hospital setting, consulting over a patient's chart.",

        "Global Racial Diversity : A Black female doctor, a Hispanic male doctor, and a South Asian male doctor in a private clinic discussing a medical case. The backdrop includes medical equipment and patient files.",

        "Generational Diversity in Healthcare: An elderly Caucasian male doctor, a middle-aged Black female doctor, and a young Hispanic male doctor in residency uniforms, in a hospital corridor discussing patient care strategies.",

        "Gender Representation in Medicine: A female doctor, a male doctor, and a non-binary doctor in a research laboratory setting, wearing lab coats and examining scientific data on a computer screen.",

        "Cultural and Religious Diversity: A Middle Eastern female doctor with a hijab, an East Asian male doctor, and an African female doctor wearing a traditional necklace, in an urban community health center consulting with patients.",

        "Ethnic and Specialty Diversity: A Native American male doctor in pediatrics, an African female doctor in oncology, and a Caucasian male doctor in dermatology, in a specialty practice setting discussing treatment plans.",

        "Age and Experience in Medicine: A young East Asian female doctor, a middle-aged Hispanic male doctor, and an elderly Black female doctor in a hospital emergency room, actively responding to emergency cases.",

        "Religious Symbolism in Healthcare: A female doctor wearing a Christian cross pin, a male doctor with a Hindu tilak, and another female doctor with a Sikh turban, in a rural medical facility discussing community health strategies.",

        "Diverse Backgrounds in Academic Medicine: A Middle Eastern male doctor, a Caucasian female doctor, and a South Asian non-binary doctor, all in academic settings, teaching a group of medical students.",

        "Inclusive Healthcare Environments: A Black female doctor, a Native American male doctor, and an East Asian non-binary doctor in an urban hospital setting, wearing lab coats and discussing patient care in a collaborative workspace."

    ],

    "Accountants": [

        "Global Professionalism: A Black female accountant with a hijab, a South Asian male accountant with a turban, and a Hispanic female accountant, all in a corporate boardroom discussing financial strategies with laptops and digital tablets in front of them.",

        "Inclusive Work Environment: A Caucasian male accountant using a wheelchair, an East Asian non-binary accountant, and a Middle Eastern female accountant, working together in an office equipped with accessibility features like adjustable desks and accessible technology.",

        "Cultural and Religious Sensitivity in the Workplace: A female accountant wearing a kippah, a male accountant in traditional African attire, and a non-binary accountant with a Sikh turban, reviewing documents in a small business setting.",

        "Gender and Age Diversity: A young transgender male accountant, a middle-aged cisgender female accountant, and an elderly non-binary accountant, all in a high-rise office setting evaluating financial data on multiple screens.",

        "Accessibility and Technology: An African male accountant with visual impairments using assistive reading technology, a Caucasian female accountant with hearing aids, and a Hispanic male accountant, all in a modern accounting firm.",

        "Diverse Backgrounds in Casual Settings: A Middle Eastern female accountant, a Native American male accountant, and an East Asian female accountant in a casual co-working space, sharing insights over coffee.",

        "Ethical and Authentic Representation: A Black non-binary accountant, a South Asian elderly female accountant, and a young Hispanic male accountant, all consulting with clients in a community center to provide pro bono financial advice.",

        "Professional and Personal Intersection: An East Asian male accountant playing chess in a break room with a Caucasian female accountant wearing a Christian cross necklace, and a Middle Eastern male accountant, highlighting personal hobbies and professional life.",

        "Real-World Scenario: A Native American female accountant, a Caucasian elderly male accountant, and a Black young female accountant in a tax preparation office, assisting diverse clients with tax returns.",

        "Visual and Cultural Diversity: A Southeast Asian male accountant, an African female accountant wearing traditional headgear, and a Caucasian non-binary accountant, all in an urban, modern accounting office discussing sustainability in finance."

    ],

    "Pharmacist": [

        "Religious and Ethnic Diversity in Pharmacy: A Black female pharmacist wearing a hijab, a Caucasian male pharmacist with a Christian cross necklace, and a South Asian male pharmacist with a Sikh turban, all consulting in a hospital pharmacy setting.",

        "Global Representation in Community Clinics: A Hispanic female pharmacist, an East Asian male pharmacist, and a Middle Eastern female pharmacist with a Star of David necklace, working together in a community clinic dispensing medications.",

        "Age and Experience in Retail Pharmacy: A young Native American female pharmacist, a middle-aged African male pharmacist, and an elderly Caucasian female pharmacist, all in a retail pharmacy discussing prescription details with customers.",

        "Gender Representation in Pharmaceutical Research: A female pharmacist, a male pharmacist, and a non-binary pharmacist in a research and development laboratory, wearing lab coats and examining clinical trial data.",

        "Cultural Sensitivity and Professionalism: A Middle Eastern male pharmacist with a turban, a Black female pharmacist with an African headscarf, and a Hispanic male pharmacist, all in a regulatory organization office reviewing drug compliance documents.",

        "Inclusive Settings in Hospital Pharmacies: An East Asian female pharmacist with a Hindu bindi, a Caucasian elderly male pharmacist, and a South Asian female pharmacist, collaborating in a hospital pharmacy preparing medications.",

        "Diverse Backgrounds in Specialty Pharmacy: A Native American male pharmacist, an African female pharmacist wearing a hijab, and a Caucasian non-binary pharmacist in a specialty pharmacy setting focusing on oncology treatments.",

        "Educational and University Health Centers: A young Hispanic male pharmacist, a middle-aged Black female pharmacist, and an elderly East Asian male pharmacist, teaching students in a university health center pharmacy.",

        "Home Care Services and Accessibility: A Middle Eastern female pharmacist with a hijab, a Black male pharmacist, and a Caucasian female pharmacist providing home care services and consulting with patients at their homes.",

        "Pharmacists in Pharmaceutical Companies: A South Asian male pharmacist, a Hispanic female pharmacist, and an African male pharmacist, working in a pharmaceutical company's lab developing new drug formulations."

    ],

    "Barista": [

        "Global Religious Representation in a Modern Café: A Middle Eastern female barista wearing a hijab, a South Asian male barista with a Sikh turban, and a Caucasian male barista wearing a kippah, all working together in a bustling urban coffee shop.",

        "Racial and Ethnic Diversity in Artisanal Café: A Black female barista, an East Asian male barista, and a Hispanic non-binary barista, crafting specialty coffees in an artisanal cafe adorned with cultural decor.",

        "Age Diversity in a Traditional Tea House: A young Native American male barista, a middle-aged African female barista, and an elderly Caucasian male barista, serving traditional teas and coffees in a vintage-style tea house.",

        "Balanced Gender Representation in a Busy Coffee Shop: A female barista, a male barista, and a non-binary barista, each showing unique styles like distinct aprons and personalized tattoos, serving a diverse clientele in a popular coffee shop.",

        "Historical and Cultural Settings at an International Coffee Festival: A Middle Eastern female barista in traditional attire, an African male barista with a distinctive hairstyle, and a Caucasian female barista, all demonstrating coffee brewing techniques at an international coffee festival.",

        "Unique Visual Attributes in a Community Café: A Hispanic male barista with sleeve tattoos, an Asian female barista with vibrant hair color, and a Black non-binary barista with unique piercings, all engaging with local customers in a community-focused cafe.",

        "Professionalism and Skill in a High-End Espresso Bar: An East Asian male barista, a South Asian female barista wearing a bindi, and a Middle Eastern male barista, all showcasing their espresso-making skills in a high-end bar setting.",

        "Cultural and Religious Sensitivity in a Specialty Coffee Shop: A female barista wearing a Christian cross necklace, a male barista with a Star of David pendant, and a non-binary barista with a visible peace symbol tattoo, working together in a specialty coffee shop that highlights organic and fair-trade coffees.",

        "Age and Experience in a Retro Café: A young African male barista, a middle-aged Hispanic female barista, and an elderly East Asian female barista, each preparing classic coffee drinks in a retro-styled cafe with vintage espresso machines.",

        "Inclusive and Respectful Representation in a Modern Tea and Coffee House: A Native American female barista, a Caucasian elderly male barista, and a Black young female barista, each expertly crafting both modern and traditional beverages, demonstrating the art and service of baristry in a harmoniously modern setting."

    ],

    "Firefighter": [

        "Cultural and Racial Diversity in Urban Emergency: A Black female firefighter wearing a hijab, a Hispanic male firefighter, and an East Asian non-binary firefighter working together to control a fire in a high-rise building in an urban setting.",

        "Religious Sensitivity in Training: A Caucasian male firefighter with a kippah, a South Asian female firefighter with a turban, and a Middle Eastern male firefighter, all in a training session practicing with fire hoses and emergency equipment.",

        "Gender Inclusivity at a Community Event: A non-binary firefighter, a female firefighter, and a male firefighter participating in a community safety workshop, demonstrating the use of fire extinguishers to local residents.",

        "Age Diversity in Rural Wildfire Fighting: A young Native American male firefighter, a middle-aged Black female firefighter, and an elderly Caucasian male firefighter working together to extinguish a wildfire in a rural area.",

        "Dynamic Rescue Operation: An African male firefighter, a Hispanic female firefighter, and an East Asian non-binary firefighter rescuing a family from a house fire, showcasing teamwork and bravery.",

        "Camaraderie and Teamwork in the Fire Station: A Middle Eastern female firefighter, a Caucasian elderly firefighter, and a South Asian male firefighter sharing a light moment at the fire station, highlighting camaraderie and teamwork.",

        "Multi-Ethnic Response Team in an Industrial Fire: A Hispanic male firefighter, a Black non-binary firefighter, and an East Asian female firefighter responding to an emergency call at an industrial site, equipped with advanced firefighting gear.",

        "Training and Skill Development: A young Caucasian female firefighter, a Middle Eastern male firefighter, and an African elderly firefighter conducting a training drill involving ladder rescues and emergency response tactics.",

        "Community Interaction and Education: A Native American female firefighter, a South Asian male firefighter with a turban, and a Hispanic male firefighter engaging with school children during a fire safety education session.",

        "Representative Team in Action: An East Asian male firefighter, a Black female firefighter wearing cultural beads, and a Caucasian non-binary firefighter working together to control a fire in a commercial area, demonstrating diverse representation and skilled teamwork."

    ],

    "Research Assistant": [

        "Diverse Lab Environment: A Muslim female research assistant wearing a hijab, a Jewish male research assistant wearing a yarmulke, and a Sikh male research assistant wearing a turban, all working together in a high-tech laboratory examining biological samples.",

        "Field Research Diversity: An Asian female research assistant, a Hispanic male research assistant, and a Black non-binary research assistant conducting environmental studies in a forest setting, collecting samples and recording data on portable devices.",

        "Age and Experience in Research: A young Black male research assistant in his twenties, a middle-aged white female research assistant, and an older Hispanic male research assistant, collaborating in an archaeological dig site, meticulously documenting findings.",

        "Gender and Racial Inclusivity in Tech Research: A white non-binary research assistant, an Asian female research assistant, and a Black male research assistant in a technology research facility, working together on advanced computing projects.",

        "Cultural Representation in Social Sciences: A Middle Eastern female research assistant wearing a hijab, a European male research assistant, and a Southeast Asian non-binary research assistant conducting social science surveys in an urban area, interacting with diverse populations.",

        "Professional and Religious Diversity: A Christian Black female research assistant, a Jewish East Asian male research assistant, and a Muslim South Asian female research assistant in a medical research lab, analyzing clinical trial data.",

        "Young Researchers in a Dynamic Setting: Three young research assistants: a Hispanic female, an African male, and a Caucasian non-binary, in a bustling university research lab, engaging in a lively discussion over a shared computer screen.",

        "Experienced Researchers in a Collaborative Effort: A team of seasoned research assistants: an elderly white male with years of experience, a middle-aged Black female specializing in genetics, and a mature Hispanic male expert in biochemistry, reviewing research findings together in a conference room.",

        "Global Health Research: An African female research assistant, a Middle Eastern male research assistant, and an East Asian non-binary research assistant in a global health research center, strategizing on pandemic response measures.",

        "Engaged and Active Research Assistants: A South Asian female research assistant wearing a bindi, a Native American male research assistant, and a European female research assistant in an engineering research facility, testing robotics and automated systems."

    ],

    "Electrical Engineers": [

        "Global Diversity in Research Lab: A Muslim female electrical engineer wearing a hijab, a Sikh male electrical engineer wearing a turban, and a Black male electrical engineer, collaborating in a high-tech electronics research lab.",

        "Dynamic Engineering Team in Manufacturing: An East Asian female electrical engineer, a Hispanic male electrical engineer, and a Middle Eastern non-binary electrical engineer, working together on a manufacturing floor testing advanced electrical systems.",

        "Inclusive Collaboration at a Corporate Office: A young African female electrical engineer, a middle-aged Caucasian male electrical engineer, and an older Hispanic female electrical engineer, in a corporate office setting discussing project timelines and designs.",

        "Field Work in Infrastructure Projects: A South Asian male electrical engineer, a Black female electrical engineer wearing professional attire, and a Native American non-binary electrical engineer, conducting field tests on electrical infrastructure in a rural setting.",

        "Innovative Start-Up Environment: Three young electrical engineers: an East Asian non-binary, a Middle Eastern female, and a Hispanic male, in a start-up environment brainstorming innovative solutions with cutting-edge technology.",

        "Experienced Engineers in a Technical Conference: An elderly Sikh male electrical engineer, a middle-aged Black female electrical engineer, and a young Caucasian male electrical engineer, presenting their research findings at an international electrical engineering conference.",

        "Advanced Circuit Design Collaboration: A Southeast Asian female electrical engineer, an African male electrical engineer, and a Caucasian non-binary electrical engineer, working together on detailed circuit designs using CAD software in a modern lab.",

        "System Testing in a High-Tech Lab: A Middle Eastern female electrical engineer, a South Asian male electrical engineer, and a Black non-binary electrical engineer, rigorously testing electrical systems and components in a state-of-the-art laboratory.",

        "Leadership and Mentorship in Engineering: A middle-aged Hispanic female electrical engineer mentoring a young Native American male electrical engineer and collaborating with an elderly East Asian male electrical engineer on leading a critical project.",

        "Cross-Cultural Team Solving Complex Problems: A Christian Caucasian female electrical engineer, a Muslim Black male electrical engineer, and a Sikh South Asian non-binary electrical engineer, engaged in a problem-solving session in an office environment."

    ],

    "Economists": [

        "Global Diversity in Corporate Setting: A Middle Eastern female economist wearing a hijab, a Sikh male economist with a turban, and a Jewish male economist wearing a yarmulke, collaborating in a corporate office with global financial data on large screens.",

        "Academic and Cultural Representation: An African female economist wearing traditional braids, a Hispanic male economist in casual attire with a visible Latin American textile scarf, and an East Asian non-binary economist, in a university classroom discussing macroeconomic theories.",

        "Government Policy Advisory: A young Caucasian male economist, an older African American female economist, and a Middle Eastern non-binary economist, in a government agency office advising on economic policies with national flags in the background.",

        "Field Research in Diverse Environments: An Indigenous female economist in rural settings conducting interviews, an Asian male economist in urban settings analyzing market behaviors, and a Black female economist in suburban areas studying economic development impacts.",

        "Economists in High-Tech Analysis: A South Asian female economist using a wheelchair, an East Asian male economist, and a Caucasian elderly economist, in a high-tech lab analyzing complex data sets on multiple digital displays.",

        "Interfaith Collaboration and Research: A Christian male economist with a cross necklace, a Hindu female economist wearing a sari and bindi, and a Sikh male economist with a beard and turban, in a research institute developing new economic models.",

        "Active Engagement in Economic Modeling: An African male economist, a Hispanic female economist, and a Middle Eastern non-binary economist, engaged in creating and analyzing economic models on whiteboards in a collaborative workspace.",

       "Presentation to Stakeholders: A young East Asian female economist, a middle-aged Black male economist, and an elderly Caucasian non-binary economist, presenting economic findings using graphs and charts in a conference room to stakeholders.",

        "Diverse Economists in Casual Brainstorming: A Southeast Asian male economist, a European female economist, and a Native American non-binary economist, in a casual setting with laptops and coffee, brainstorming on economic sustainability projects.",

        "Inclusivity in Economic Education: An elderly Black male economist, a young Hispanic female economist, and a Middle Eastern female economist in a hijab, teaching a diverse group of students in a university setting, using digital tablets and economic textbooks."

    ],

    "Architect": [

        "Religious and Ethnic Representation in Design Studio: A Muslim female architect wearing a hijab, a Sikh male architect wearing a turban, and a Jewish male architect wearing a kippah, collaborating in a high-tech design studio using advanced software for 3D modeling and visualization. The setting includes modern architectural tools and a dynamic workspace, emphasizing diversity and inclusivity in professional environments.",

        "Diverse Urban Planners in a Meeting: A Black female architect, an Asian male architect, and a Hispanic non-binary architect in an urban planning session, focusing on sustainable development and community engagement. The environment is a modern office with cityscape models and digital screens displaying urban layouts, showcasing a multicultural team working on city improvement projects.",

        "Cross-Generational Collaboration on a Construction Site: A young Caucasian male architect, a middle-aged African female architect, and an elderly Hispanic male architect on a construction site, supervising building progress and discussing with engineers. The scene captures them in hard hats with blueprints, embodying a cross-generational, diverse professional team.",

        "Sustainable Design Experts in a Workshop: An East Asian female architect, a South Asian male architect, and a Middle Eastern female architect, all experts in sustainable design, in a workshop discussing eco-friendly materials. The setting includes samples of sustainable resources and architectural drafts, emphasizing their roles as sustainability consultants.",

        "Innovative Project Team in a Design Startup: A young Native American male architect in an innovative design startup discussing a new project with a middle-aged Caucasian female architect and an elderly East Asian non-binary architect. The office is filled with digital displays and conceptual models, highlighting a vibrant and creative atmosphere.",

        "Architects Reviewing Historical Renovation Plans: A Middle Eastern male architect, a Black female architect, and a Caucasian non-binary architect specializing in the restoration of historical buildings, reviewing renovation plans in a design studio. The setting includes architectural drawings of historical structures and a discussion over preserving architectural heritage.",

        "Client Presentation by Diverse Architects: A Hispanic male architect, an African female architect, and an East Asian male architect presenting a building proposal to clients. The environment is a professional conference room with digital presentations and physical models, showcasing their collaborative approach and client engagement strategies.",

        "Technical Detailing Session in an Architectural Firm: A Southeast Asian female architect, a Native American male architect, and a Caucasian elderly female architect focusing on the technical details of a building design, examining material specifications and structural integrity in an architectural firm’s technical department.",

        "Cultural Diversity in Community Development Projects: An African male architect, a Hispanic female architect, and a South Asian non-binary architect working on community development projects in a collaborative office environment. The scene includes plans for residential areas and community centers, emphasizing their contributions to socially responsible architecture.",

        "Architects Engaging in Creative Brainstorming: A Middle Eastern female architect, a Black young male architect, and an elderly Caucasian female architect in a creative brainstorming session at a modern co-working space. The setting includes sketchpads, architectural models, and a lively discussion, highlighting creativity and diverse perspectives in architectural design."

    ],

    "Librarian": [

        "Interfaith Librarian Collaboration: A Muslim female librarian wearing a hijab, a Jewish male librarian wearing a kippah, and a Sikh male librarian wearing a turban, working together in a modern, technology-integrated library setting, showcasing a harmonious interfaith collaboration.",

        "Diverse Librarians in Community Engagement: A Black female librarian, a Hispanic male librarian, and an Asian non-binary librarian engaging with community members in a traditional library setting, conducting a story time session for children, emphasizing inclusivity and community outreach.",

        "Generational Diversity in Librarianship: A young Caucasian male librarian in his 20s, a middle-aged African female librarian, and an elderly Hispanic male librarian over 60, working together in a library equipped with both traditional books and digital resources, highlighting the span of generations in the profession.",

        "Librarians in Tech-Integrated Environment: An East Asian female librarian, a South Asian male librarian, and a Middle Eastern female librarian in a modern library setting, using digital resources like e-readers and educational software to assist patrons, demonstrating the technological evolution of libraries.",

        "Librarians Leading Educational Programs: A Native American female librarian, a Caucasian elderly female librarian, and a Black young male librarian conducting a tech-based learning session in a library, with laptops and interactive displays, fostering an educational and engaging atmosphere.",

        "Cultural Diversity in Librarian Attire: A Middle Eastern male librarian with a turban, an African female librarian with an African headscarf, and a Hispanic male librarian, all in a vibrant library setting reviewing books and resources, celebrating cultural diversity through their attire and expertise.",

        "Non-Binary and Gender Diversity: A non-binary librarian with a visible peace symbol tattoo, a female librarian with a Christian cross necklace, and a male librarian in professional attire, managing a library’s information desk, focusing on gender diversity and inclusive service.",

        "Librarians in Specialized Settings: A Southeast Asian female librarian in a medical library, a Caucasian male librarian in a law library, and an African male librarian in a university library, each using specialized resources to assist students and professionals, showcasing their expert knowledge.",

        "Youthful and Dynamic Librarians: Three young librarians—a Hispanic female, an African male, and a Caucasian non-binary—all in their late 20s, working in a bustling urban library, using tablets to interact with patrons and manage library operations, reflecting the dynamic nature of modern librarianship.",

        "Senior Librarians Sharing Wisdom: An elderly East Asian male librarian, a Middle Eastern female librarian, and a South Asian male librarian, all seasoned professionals, sharing insights and wisdom in a library setting, guiding younger librarians and patrons, emphasizing lifelong learning and mentorship."

    ]

}

professions_prompts.keys()

from diffusers import AutoPipelineForText2Image
import torch
import os

# Load the pipeline
pipe = AutoPipelineForText2Image.from_pretrained("sd-legacy/stable-diffusion-v1-5", torch_dtype=torch.float16, variant="fp16")
pipe.to("cuda")
#stabilityai/sdxl-turbo
# List of nurse descriptions

for key in professions_prompts.keys():
  k=key
  prompt=professions_prompts[key]
# Loop through each description
  for description in prompt:
      print(description.split(': ')[1])
      a=description.split(': ')[1]
      # Format the prompt
      #prompt = f"a photo of headshot of {description.split(': ')[1]}"
      prompt = "a photo of" +" "+ a
      #prompt = f"a photo of {description.split(': ')[1]}"  # Extract the description part after the label

      # Generate the image
        # Adjust num_inference_steps and guidance_scale as needed
      #image = pipe(prompt=prompt, num_inference_steps=50, guidance_scale=7.5).images[0]
      image = pipe(prompt=prompt, num_inference_steps=150, guidance_scale=7.5).images[0]
      # Save the image
      filename = description.split(':')[0].replace(' ', '_') + '.png'
      path=string = '/data/home/ours-multi-v1/' + str(k) + '/'
      os.makedirs(path, exist_ok=True)
      image.save('/data/home/ours-multi-v1/'+ str(k) + '/'+ str(filename))
