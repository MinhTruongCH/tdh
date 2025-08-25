# Data Engineer Technical Test - Terre des hommes

### Setup Instructions

 Create a python virtual environment and make sure that you will install all the libraries you need in this virtual env. Also generate a `requirements.txt` file with the exact versions of the libraries you are using during the test.

 For this test you can use and are encouraged to use internet and AI.

### Data

In the `/data` folder, you will find three files representing our fundraising activities. It's synthetic fake data and will be used as source for the test.

### Delivrable

The goal of this test is to evaluate how you navigate through technical problems and how you would present your work to the Business Analyst that will be working with you. Therefore in addition to the code, we ask you to create a slide deck to present your results. This presentation will be evaluated with great attention.

At the end of the test you should export your presentation as a PDF and put it in folder `/presentation`.

The code should be placed in folder `/src`.

To upload your delivrable please package your whole folder as a zip file and generate a download link on https://www.swisstransfer.com/en-ch. Then input the link on the test platform answer input. Make sure that the expiration duration of the link is at least 30 days.

### The Test: 3 Parts

#### Part 1: Building the Data Model

Your first task is to get your hands on the data and understand by yourself what they represent. The goal is to have a structured dataset ready for analysis. To do that you can either use python or dbt with a duckdb adaptor.

**Note:** High bonus if you use `dbt` with a `duckdb` adaptor to perform these transformations as it's a very modern approach

**Tasks:**
1.  Load the data from the CSV, Parquet, and JSON files.
2.  Perform necessary cleaning and transformations.

**Presentation**: L
- You should include a data model diagram in the presentation to explain the data model

---

#### Part 2: Answering Business Questions (30 minutes)

Using the data model you prepared in Part 1, answer the following business questions. Your analysis should be presented in the slides.

**Questions:**
1.  **Lifetime Value (LTV)**: What is the average LTV of a donor?
2.  **Retention & Churn**: Calculate the annual donor retention rate. For example, what percentage of donors who gave in 2022 also gave in 2023?
3.  **Causality Analysis**: On **June 1, 2024**, we launched a major social media campaign. Using causal inference (we recommand the [`causalimpact`](https://github.com/WillianFuks/tfcausalimpact) Python library), analyze its effect on the daily number of donations. Present your findings and conclude if the campaign was successful in increasing donations.

**Presentation**
*   A few slides or a diagram explaining your findings for each question. The visuals should be clear and easy for a non-technical stakeholder to understand.

---

#### Part 3: Open-Ended Data Project

This is your opportunity to be creative. Suggest more KPIs, advanced analysis, or ML approaches that you believe could improve the marketing and fundraising strategy of Tdh. You can start implementing them and showcase some results if you have time.

**Task:**
Based on the available data, identify key opportunities. Develop a prototype or proof-of-concept to address it if possible.

**Presentation**
*   Slides or a diagram explaining your initiative goal, your methodology, and the potential business impact for Tdh.

#### Final Checks
- [ ] Your code is concise and well-commented so that the evaluator can understand your logic.
- [ ] You have included clear instructions on how to run your code, either in the comments or in a markdown file.
- [ ] All deliverables are in the correct folders.
- [ ] requirements.txt is defined

Thank you for your time and effort. We look forward to reviewing your work!
