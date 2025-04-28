import streamlit as st
import pandas as pd

st.set_page_config(page_title="Diabetic Retinopathy Home", layout="wide")

st.image("dr_stages.jpg", caption="Stages of Diabetic Retinopathy: Mild NPDR, Moderate NPDR, Severe NPDR with macular edema, Proliferative DR, Advanced Proliferative DR", use_column_width=True)

st.markdown("""
# About Diabetic Retinopathy

> **Diabetic retinopathy** is a complication of diabetes that affects the eyes and can lead to vision loss if not detected and treated early.

- **Every newly diagnosed diabetic** should be screened for retinopathy at the time of diagnosis and at least annually thereafter.
- **Early detection and management** can prevent vision loss.

**Screening Recommendations:**
- All diabetic patients should undergo a comprehensive eye examination, including visual acuity and fundus examination.

[ICMR Standard Treatment Workflow (PDF)](https://www.icmr.gov.in/icmrobject/uploads/STWs/1726569102_diabetic_retinopathy.pdf)
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Table 1: Classification of Diabetic Retinopathy**")
    dr_table = pd.DataFrame([
        ["No Apparent Retinopathy", "No Abnormalities", "Review in 1 year"],
        ["Mild NPDR", "Microaneurysms only", "Refer to retina specialist"],
        ["Moderate NPDR", "More than just microaneurysms, but less than severe NPDR", "Refer to retina specialist"],
        ["Severe NPDR", "Any of: Intra-retinal haemorrhages (≥20 in each quadrant); Definite venous beading (in 2 quadrants); Intra-retinal microvascular abnormalities (in 1 quadrant); No signs of proliferative retinopathy", "Refer to retina specialist"],
        ["Proliferative DR", "Neovascularization, vitreous/pre-retinal haemorrhage", "Refer to retina specialist"],
    ], columns=["Type", "Findings on Dilated Ophthalmoscopy", "Referral*"])
    st.table(dr_table)

with col2:
    st.markdown("**Table 2: Classification of Diabetic Macular Edema**")
    dme_table = pd.DataFrame([
        ["DME Absent", "No retinal thickening or hard exudates in posterior pole", "Review in 1 year"],
        ["Mild DME", "Retinal thickening or hard exudates in posterior pole but outside the central subfield of the macula (diameter 1000 µm)", "Refer to retina specialist"],
        ["Moderate DME", "Retinal thickening or hard exudates within the central subfield of the macula but not involving the centre point", "Refer to retina specialist"],
        ["Severe DME", "Retinal thickening or hard exudates involving the centre of the macula", "Refer to retina specialist"],
    ], columns=["DME Type", "Findings on Dilated Ophthalmoscopy", "Referral*"])
    st.table(dme_table)

st.markdown("---")

st.markdown("**Management Workflow**")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    **PHC/Primary Level**
    - Detailed history & examination
    - Refraction for BCVA
    - Preliminary diagnosis
    - Referral to Ophthalmologist (as per Table 1 and 2)
    - Counselling regarding metabolic control
    - Preventive advice, counselling and regular follow up
    """)
with col2:
    st.markdown("""
    **Secondary Level**
    - Refraction for BCVA
    - Detailed work up including indirect ophthalmoscopy
    - Diagnose, classify, advice (as per Table 1 and 2)
    - Point to point guided referral
    - Ensure follow up and compliance
    """)
with col3:
    st.markdown("""
    **Tertiary Level**
    - Counselling regarding metabolic control and systemic comorbidities (hypertension, nephropathy)
    - Diagnose, classify, advice (as per Table 1 and 2)
    - Intravitreal injections/laser photocoagulation/vitreoretinal surgery
    - Ensure postoperative follow up and compliance including collaboration with district hospital ophthalmologists
    """)

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.error("""
    **Indications for Urgent Referral:**
    - Vision loss
    - Hard exudates
    - Non-dilating pupil
    - Blurred disc margins
    - No view of fundus
    - Haemorrhages
    """)
with col2:
    st.warning("""
    **Indications for Surgery:**
    - Sudden vision loss
    - Absent Foveal Reflex
    - Clinically recognizable macular edema
    - Rubeosis iridis
    - Proliferative DR
    """)

st.markdown("---")

st.info("""
**Abbreviations**
- **BCVA:** Best corrected visual acuity
- **DME:** Diabetic macular edema
- **FFA:** Fundus fluorescein angiography
- **IOP:** Intra ocular pressure
- **OCT:** Optical coherence tomography
- **OCTA:** Optical coherence tomography angiography
""") 