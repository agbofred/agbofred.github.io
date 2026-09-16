---
title: "CS 480W/481: Course Syllabus"
author: "Professor Fred Agbo, PhD"
date: "August 2026"
format:
  html:
    include-after-body: assets/toc-scrollspy-fix.html
    css: assets/custom-theme.css
    toc: true
    toc-depth: 3
---
<!-- 
# CS 480W/481: Senior Capstone Project I & II

**Computer Science Capstone**

**AUTHOR**  
Professor Fred Agbo, PhD

**PUBLISHED**  
August 2026

--- -->

# Course Information

## Basic Information

| | |
|---|---|
| Course Numbers | CS 480W (Fall 2026) / CS 481 (Spring 2027) |
| Credits | 4 credits per semester (8 total) |
| Duration | Two semesters (30 weeks) |
| Meeting Format | Fridays 10:30–11:00 AM (group, 30 min) + Individual sprint review (15 min, by appointment) |
| Prerequisites | Senior standing; completion of core CS curriculum |

## Professor

**[Professor Fred Agbo, PhD](https://fredagbo.com/)**  
Email: [fjagbo@willamette.edu](mailto:fjagbo@willamette.edu)  
Office: Ford Hall 209 (Salem)

## Office Hours

Office hours are available by 15-minute appointments or on a drop-in basis when available. Multiple modalities are offered (in-person, phone, Google Meet). If the scheduled times do not align with your availability, please contact the instructor.

## Course Description

A two-semester culminating experience where students apply their cumulative knowledge to design, develop, and deploy a full-stack or similar-type application. Students will follow industry-standard software development lifecycle (SDLC) practices, from initial conception through final deployment and documentation. The course emphasizes professional software engineering methodology, project management, technical communication, and collaborative development practices.

## Learning Objectives

Upon completion of this course sequence, students will be able to:

1. Design and implement a complete full-stack or similar-type application from conception to deployment
2. Apply software engineering principles and best practices throughout the development lifecycle
3. Demonstrate proficiency in project management and agile methodologies
4. Create comprehensive technical documentation
5. Present technical work to both technical and non-technical audiences
6. Collaborate effectively using version control and project management tools
7. Conduct meaningful peer reviews and incorporate feedback

## Textbooks and Materials

| | | |
|---|---|---|
| Software Engineering: A Modern Approach | Marco Tulio Valente. Free, open textbook. Available [here](https://softengbook.org/) | Recommended |
| Handbook of Software Engineering Methods | Lara Letaw. Free OER via Open Textbook Library. Available [here](https://open.umn.edu/opentextbooks/textbooks/1557) | Recommended |

*Software Engineering: A Modern Approach* provides comprehensive coverage of software engineering topics including process models, requirements, architecture, design, testing, and maintenance. *Handbook of Software Engineering Methods* complements it with a practical, methods-oriented framing aligned with real-world project work. Both texts are free and open-access.

---

# Software Development Methodology

## Modified Agile with Academic Milestones

This course employs a Modified Agile methodology that combines industry-standard Agile practices with academic milestone requirements.

### Core Principles

1. **Iterative Development:** Features built incrementally with regular feedback loops
2. **Weekly Sprints:** One-week development cycles aligned with instructor meetings
3. **Continuous Integration:** Code integrated and tested regularly
4. **Adaptive Planning:** Requirements evolve based on feedback and learning
5. **Stakeholder Engagement:** Instructor as product owner (or external customer in certain situations) and peers as stakeholders

## Development Cycle Structure

### Weekly Sprint Cycle

The following provides a high-level overview of the weekly sprint cycle. The precise schedule may vary based on project needs and progress.

| | | |
|---|---|---|
| Monday | Sprint planning | Sprint backlog |
| Tuesday–Thursday | Development work | Code commits |
| Friday | Code review and testing | Pull requests |
| Weekend | Documentation and reflection | Updated docs |
| Weekly Meeting | Sprint review with instructor | Demo |
### Scrum Artifacts (Academic Adaptation)

1. **Product Backlog:** Living document in GitHub Issues
2. **Sprint Backlog:** Weekly task list with estimates
3. **Burndown Charts:** Visual progress tracking
4. **Definition of Done:** Explicit completion criteria

## Required Development Practices

### Version Control Requirements

- Daily commits minimum (including research/documentation days)
- Commit format: Conventional commits (`feat:`, `fix:`, `docs:`, etc.)
- Workflow: Feature branch with pull requests
- Protection: Main branch requires review

### Testing Strategy

| | | |
|---|---|---|
| Unit Tests | All public methods | 60% minimum (Semester 2) |
| Integration Tests | All API endpoints | 100% |
| End-to-End Tests | Critical user paths | Core features |
| Performance Tests | Database queries | < 100ms response |

### CI/CD Pipeline

A continuous integration and continuous deployment (CI/CD) pipeline will be established to automate testing and deployment processes, ensuring rapid and reliable delivery of software updates. The implementation will vary based on the project's technical stack.

Example workflow configuration for GitHub Actions:

```yaml
name: CI/CD Pipeline
on: [push, pull_request]
jobs:
  test:
    - run: npm test
    - run: npm run coverage
  deploy:
    - staging: automatic
    - production: manual approval
```

## Agile Ceremonies

### Sprint Planning (Weekly – 10 min)

- Review velocity
- Select backlog items
- Break down tasks
- Commit to goals

### Daily Standup (Asynchronous)

Post daily by 10 AM in Discord/Slack:

1. Yesterday's completions
2. Today's plan
3. Current blockers

### Sprint Review (Weekly – 15 min)

Each student must individually book a 15-minute Sprint Review meeting with the instructor every week via Google Calendar:

**[Book Your Sprint Review](https://calendar.app.google/QMJ1TL3GWyFNkK5eA)**

- Demo features
- Gather feedback
- Discuss incomplete items

### Sprint Retrospective (Bi-weekly – 5 min)

- What went well
- Areas for improvement
- Action items

---

# Course Structure

## Weekly Meeting Schedule

The course uses two meeting modalities throughout the semester:

### Group Review Session (Every Friday, 10:30–11:00 AM)

A 30-minute group session held **every Friday from 10:30 to 11:00 AM at Ford Hall 209**. All students are expected to attend. This session is used for:

- Reviewing expectations and discussing the week's milestones as shown in the implementation schedule below
- Group-level sprint check-in and discussion
- Peer collaboration and shared problem-solving

### Individual Sprint Review (Weekly – 15 min, By Appointment)

In addition to the group session, **every student must individually book a 15-minute one-on-one Sprint Review** with the instructor each week. Use the link below to reserve your time slot:

**[Book Your Individual Sprint Review →](https://calendar.app.google/QMJ1TL3GWyFNkK5eA)**

> Each student is responsible for booking their own slot. These sessions are used to demo individual progress, receive personalized feedback, and address sprint-specific blockers.

---

## Semester 1: Planning, Design, and Foundation (CS 480W – Fall 2026)

### Milestone 1: Project Initiation and Planning (Weeks 1–4)

| Week | Topic | Deliverable |
|------|-------|-------------|
| 1 | Course Introduction and Project Brainstorming: course overview, SDLC methodologies review, project ideation workshop | Three project ideas (one page each) |
| 2 | Project Selection and Feasibility: technology stack research, feasibility analysis, market research | Project selection with justification |
| 3 | Project Proposal Development: scope definition, user stories, risk assessment | Draft project proposal |
| 4 | Proposal Finalization: proposal refinement, timeline planning, methodology selection | Final project proposal (5–7 pages) |

### Milestone 2: Design and Architecture (Weeks 5–8)

| Week | Topic | Deliverable |
|------|-------|-------------|
| 5 | System Architecture Design: high-level architecture, component diagrams, database schema | Architecture diagram |
| 6 | UI/UX Design: wireframes, user flows, accessibility planning | Complete wireframe set |
| 7 | Detailed Design: API specifications, data flow diagrams, security architecture | Technical design document |
| 8 | Mid-Semester Presentation: present to instructor and peers, peer feedback, Q&A | 15-minute presentation |

### Milestone 3: Foundation Development (Weeks 9–14)

| Week | Focus Area | Deliverable |
|------|-----------|-------------|
| 9 | Environment Setup | CI/CD pipeline |
| 10 | Database Implementation | Schema with test data |
| 11 | Backend Foundation | Auth system and core APIs |
| 12 | Frontend Foundation | Basic UI with routing |
| 13 | Integration | Working prototype |
| 14 | Documentation | Complete code docs |

### Milestone 4: Semester 1 Wrap-up (Week 15)

- Working prototype demonstration
- Semester retrospective
- Semester 2 planning
- **Deliverable:** Prototype demo and reflection paper

## Semester 2: Development, Testing, and Deployment (CS 481 – Spring 2027)

### Milestone 5: Feature Development (Weeks 1–6)

- Week 1: Sprint planning and setup
- Weeks 2–3: Core Feature Sprint 1
- Weeks 4–5: Core Feature Sprint 2
- Week 6: Integration testing and fixes

### Milestone 6: Testing and QA (Weeks 7–10)

| Week | Focus | Deliverable |
|------|-------|-------------|
| 7 | Test Planning | Test cases, scripts |
| 8 | Mid-Semester Presentation | Technical demo |
| 9 | User Acceptance Testing | 5+ user sessions |
| 10 | Refinement Sprint | Priority fixes |

### Milestone 7: Deployment and Documentation (Weeks 11–13)

- Week 11: Production environment setup
- Week 12: Deployment and monitoring
- Week 13: Final documentation package

### Milestone 8: Project Closure (Weeks 14–15)

- Week 14: Showcase preparation
- Week 15: Public presentation and handoff

---

# Peer Review Process

## Overview

Each student serves as a peer reviewer for two projects throughout both semesters, developing critical evaluation skills and exposure to different approaches.

## Review Partnerships

Review partnerships are assigned at the start of Semester 1 and remain consistent throughout both semesters. Each student provides constructive feedback and support to their assigned peers.

## Review Schedule

### Semester 1 Reviews

1. Week 3: Proposal Draft
2. Week 6: Architecture
3. Week 8: Design Docs
4. Week 11: Backend Code
5. Week 13: Frontend Code
6. Week 15: Prototype

### Semester 2 Reviews

1. Week 2: Sprint Planning
2. Week 5: Features
3. Week 8: Presentation
4. Week 9: Testing
5. Week 11: Deployment
6. Week 12: Documentation
7. Week 14: Final Code
8. Week 15: Showcase

## Review Rubric

| Grade | Description | Range |
|-------|-------------|-------|
| A | Specific, actionable feedback with code examples | 90–100% |
| B | Identifies major issues with useful suggestions | 80–89% |
| C | Meets requirements with basic feedback | 70–79% |
| D | Minimal effort, vague feedback | 60–69% |
| F | Missing or non-constructive | Below 60% |

---

# Assessment and Grading

## Grade Scale

| | | | |
|---|---|---|---|
| ≥ 92.00 | A | 72.00 – 77.99 | C |
| 90.00 – 91.99 | A- | 70.00 – 71.99 | C- |
| 88.00 – 89.99 | B+ | 68.00 – 69.99 | D+ |
| 82.00 – 87.99 | B | 62.00 – 67.99 | D |
| 80.00 – 81.99 | B- | 60.00 – 61.99 | D- |
| 78.00 – 79.99 | C+ | ≤ 59.99 | F |

## Semester 1 Grade Distribution (CS 480W)

| Component | Weight | Description |
|-----------|--------|-------------|
| Project Proposal | 15% | Complete proposal document |
| Design Documentation | 15% | Architecture and design docs |
| Weekly Progress | 20% | Meeting attendance and progress |
| Mid-Semester Presentation | 10% | Design presentation |
| Working Prototype | 25% | Functional MVP |
| Final Presentation | 10% | Semester wrap-up |
| Peer Reviews | 5% | Quality of reviews provided |

## Semester 2 Grade Distribution (CS 481)

| Component | Weight | Description |
|-----------|--------|-------------|
| Feature Completion | 25% | All planned features implemented |
| Testing and Quality | 15% | Test coverage and bug fixes |
| Deployment Success | 15% | Production deployment |
| Documentation | 15% | User and technical docs |
| Weekly Progress | 15% | Consistent development |
| Final Presentation | 10% | Project showcase |
| Peer Reviews | 5% | Quality of reviews provided |

---

# Required Tools and Resources

## Technology Stack

- **Version Control:** Git/GitHub (required)
- **Project Management:** Jira, Trello, or GitHub Projects
- **Communication:** Discord or Slack
- **CI/CD:** GitHub Actions, Jenkins, or CircleCI
- **Cloud:** Student credits for AWS/Azure/GCP
- **Documentation:** Markdown, JSDoc, or Sphinx

## Development Environment

```bash
# Minimum required setup
git --version      # 2.0+
node --version     # 14.0+ (if using Node.js)
docker --version   # 20.0+ (recommended)
```

---

# Project Proposal Template

**DEPARTMENT OF COMPUTER SCIENCE**

## Senior Capstone Project Proposal

**[Working Project Title]**

> A title is required even in draft form. Use a placeholder that names the problem or system (for example, “A Mobile App for Campus Food-Pantry Scheduling”) rather than “My Capstone Project.”

**Student Name(s):**  
**Team / Group Number (if applicable):**  
**Faculty Advisor:**  
**Course / Section:**  
**Submission Date:**  

### How to Use This Template

This is a working document, not a final contract. Each section includes a prompt describing what a reviewer expects to see. Write your best current thinking underneath each one, even if it is rough, incomplete, or likely to change. A proposal with honest gaps and open questions is more useful, and more gradable, than one that hides uncertainty behind vague language.

**Target length:** Approximately 5 pages, excluding the title page and references, single-spaced, 11–12 pt font.

## 1. Problem Statement and Motivation

> Describe, in plain language, the real problem or unmet need your project addresses and why it matters to actual users or stakeholders.
>
> Consider who experiences this problem today, how they currently cope without your solution, and what evidence (personal experience, articles, data, interviews) suggests the problem is real and worth solving.

## 2. Project Overview

> Summarize, in 3–5 sentences, what you plan to build or investigate, as if explaining it to a classmate outside the CS department.
>
> Consider naming the type of artifact (web app, mobile app, ML model, systems tool, research study, etc.) and the single core function it must perform.

## 3. Goals and Objectives

> List the specific, measurable objectives your finished project should achieve, distinguishing must-have goals from stretch goals.
>
> Phrase each objective so a reader could later check whether it was met. For example: “Users can upload a file under 10MB and receive results in under 5 seconds.”

## 4. Scope and Boundaries

> Clarify what is explicitly included in this project and what is explicitly excluded, to prevent scope creep later.

**In scope:** The features, platforms, or use cases you commit to delivering by the deadline.

**Out of scope:** Related ideas you are consciously setting aside for a future version or a different project.

## 5. Technical Approach and Methodology

> Outline your current best guess at the technologies, architecture, algorithms, or methods you expect to use, and how you will verify that the result works.
>
> Consider languages and frameworks under consideration, major components or modules, data sources, and how you will test or evaluate correctness and performance.
>
> This section may be tentative. Flag the specific technical decisions still open and what you need to learn or prototype to resolve them.

## 6. Related Work and Existing Solutions

> Briefly identify at least two or three existing tools, products, papers, or approaches that address a similar problem, and state how your project will differ or improve on them.
>
> Consider using a short table or bullet list comparing each alternative’s strengths and limitations against your intended approach.

## 7. Timeline and Milestones

> Break the semester into 4–6 milestones with target dates and a one-line deliverable for each, working backward from the final deadline.

| Target Date | Milestone / Deliverable | Status |
|-------------|-------------------------|--------|
|             |                         |        |
|             |                         |        |
|             |                         |        |
|             |                         |        |
|             |                         |        |

## 8. Anticipated Challenges and Risks

> Name the two or three biggest things that could go wrong (technical, scheduling, data access, scope) and your current plan for handling each.
>
> Consider a simple risk / mitigation pairing rather than a general worry. For example: “Risk: needed dataset may be restricted. Mitigation: identify a public substitute by week 3.”

## 9. Expected Outcomes and Deliverables

> List the concrete artifacts you will hand in at the end of the semester, such as source code, a deployed demo, a final report, a poster, or a dataset.

## 10. Resources and Support Needed

> Note any hardware, software licenses, datasets, cloud credits, faculty expertise, or external partners this project will require.

## 11. References

> Cite any articles, tools, APIs, or prior work referenced above, using a consistent citation style such as IEEE or ACM.

---

# Course Policies

## Academic Integrity

All code must be original or properly attributed. AI tool usage must be documented. Plagiarism results in course failure. For details, consult Willamette's academic integrity policy.

## Late Work

Students are allotted 72 cumulative hours (3 days) of late submissions across all deliverables without penalty. Hours may be distributed across assignments as needed. Once exhausted, late submissions incur a 20% penalty per 24 hours on a continuous scale; deliverables submitted more than 5 days late receive no credit. Extenuating circumstances should be discussed with the instructor promptly.

## Incomplete Grades

Incomplete grades are granted only for prolonged illness or family emergencies that remove a student from the learning environment for an extended period. Incompletes are not granted for falling behind due to motivation, comprehension, or time management difficulties. Students experiencing academic difficulties should consult with the instructor to develop an improvement plan.

## Time Commitment

Per Willamette's Credit Hour Policy, each hour of class time requires 2–3 hours of work outside class. The advanced nature of this course requires consistent effort throughout the semester. Expect 6–9 hours per week of outside engagement including development, documentation, and project work.

## Classroom Conduct

Constructive classroom behavior supports an environment of trust, respect, and collaborative learning. Disruptive behaviors include but are not limited to: interrupting others, distracting from course content, unauthorized recordings, and any form of harassment or abuse. Such behaviors will not be tolerated.

## Accommodations

Students requiring accommodations should provide documentation from Accessible Education Services (Smullin 155, 503-370-6737, accessible-info@willamette.edu) within the first two weeks.

## Office Hours

- **By Appointment:** Project-specific consultations
- **Online:** Discord server for async questions

---

# Appendix: Additional Resources

## Recommended Reading

1. *The Pragmatic Programmer* by Hunt and Thomas
2. *Clean Code* by Robert Martin
3. *Design Patterns* by the Gang of Four

## Online Resources

- [GitHub Docs](https://docs.github.com/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [Stack Overflow](https://stackoverflow.com/)
- [DevDocs](https://devdocs.io/)

## Success Tips

1. Start early and iterate often
2. Commit code daily, even small changes
3. Ask for help when stuck for more than 2 hours
4. Attend all weekly meetings prepared
5. Engage meaningfully in peer reviews
6. Document as you go, not at the end

---

# University Policies

## Inclusive Classroom

Students are addressed by their affirmed name and pronouns upon request. Notify the instructor at any point to update records accordingly.

## Accessibility and Accommodations

Willamette University is committed to creating inclusive learning environments. Students experiencing barriers to inclusion or achievement should notify the instructor promptly. Students with disabilities are encouraged to contact Accessible Education Services (Smullin 155, 503-370-6737, accessible-info@willamette.edu) to discuss accommodations.

## Title IX

Willamette University prohibits discrimination and harassment based on sex or gender. As a mandatory reporter, the instructor is required to report any incidents of sexual misconduct disclosed to them to Willamette's Title IX Coordinator. For confidential support, contact:

- Confidential advocate: confidential-advocate@willamette.edu
- WUTalk crisis line: 503-375-5353
- Campus Safety (emergency): 503-370-6911

## Religious Accommodations

Students requiring accommodations for religious observances should notify the instructor within the first two weeks of the semester.

## Land Acknowledgement

We respectfully acknowledge that Willamette University is located on the ancestral lands of the Kalapuya people, who today are represented by the Confederated Tribes of the Grand Ronde and the Confederated Tribes of the Siletz Indians. We honor their deep connection to this land and recognize the ongoing contributions of Indigenous peoples to our academic community.

---

**Course materials structure adapted from [Dr. Lucas P. Cordova's CS Capstone course](https://lucascordova.phd).** Special thanks to Lucas for the excellent organizational framework to capstone education.

---

**Note:** This syllabus is subject to change with reasonable notice. Students will be informed of any significant changes via official communication channels.

---

*Last updated: August 2026*
