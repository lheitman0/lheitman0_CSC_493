from transformers import AutoTokenizer
import transformers
import torch

model = "xz97/AlpaCare-llama2-7b"

tokenizer = AutoTokenizer.from_pretrained(model)
'''
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

sequences = pipeline(
    #"You are given a series of tasks and the description of a clinical trial. Come up with additional tasks that ask questions about the trial, similar to the provided tasks. \nDescription: Introduction: Glass ionomer cements (GICs) are widely used in clinical dentistry due to their advantageous properties. However, they present inferior physical and mechanical properties compared to resin composites. Various techniques have been suggested to improve properties of conventional GICs such as radiant heat transfer by Light Emitting Diode (LED) or lasers, ultrasonic energy transfer also using of (CaCl2) solution. Aim: Clinical evaluation of chemically cured conventional glass ionomer after light-emitting diode radiant heat enhancement. . Methodology: Eighteen healthy patients with 36-second molar teeth will be selected where each patient should have two oclusso- mesial cavities. Standardized oclusso- mesial cavities will be prepared for all the selected teeth, for each patient the first tooth will be restored with chemically cured conventional GICs without any enhancement (M1 group). Meanwhile, the second tooth will be restored by chemically cured conventional GICs that enhanced with radiant heat (LED) (M2 group). functional and biological criteria of each restoration will be clinically evaluated immediately after restoration (T0), six months later (T1), and after 12 months (T2) using Federation Dentaire International (FDI) criteria for assessment of dental restorations. \nTask 1: Come up with a title for the described clinical trial. \nTask 2: Is it a randomized study? \nTask 3: What findings are to be expected? \nTask 4: Would the trial perform better if only tested on healthy participants?\n Task 4:",
    #"Come up with a title for the following clinical trial:\nDescription: Introduction: Glass ionomer cements (GICs) are widely used in clinical dentistry due to their advantageous properties. However, they present inferior physical and mechanical properties compared to resin composites. Various techniques have been suggested to improve properties of conventional GICs such as radiant heat transfer by Light Emitting Diode (LED) or lasers, ultrasonic energy transfer also using of (CaCl2) solution. Aim: Clinical evaluation of chemically cured conventional glass ionomer after light-emitting diode radiant heat enhancement. . Methodology: Eighteen healthy patients with 36-second molar teeth will be selected where each patient should have two oclusso- mesial cavities. Standardized oclusso- mesial cavities will be prepared for all the selected teeth, for each patient the first tooth will be restored with chemically cured conventional GICs without any enhancement (M1 group). Meanwhile, the second tooth will be restored by chemically cured conventional GICs that enhanced with radiant heat (LED) (M2 group). functional and biological criteria of each restoration will be clinically evaluated immediately after restoration (T0), six months later (T1), and after 12 months (T2) using Federation Dentaire International (FDI) criteria for assessment of dental restorations.",
    "<s>[INST] <<SYS>>Predict if this trial will transition to the next phase. Return the answer as the corresponding label: Yes or No.<</SYS>>TRIAL NAME: Phase II - CLN-PRO-V004; BRIEF: This study will evaluate how well Humacyte's Human Acellular Vessel (HAV) works when surgically implanted into a leg to improve blood flow in patients with peripheral arterial disease (PAD). This study will also evaluate how safe it is to use the HAV in this manner. ; DRUG USED: Humacyl[/INST]",
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=200,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")
'''

# Run text generation pipeline with our next model
sys = "How common is the Turner syndrom in the US population?"
prompt = ''#"BRIEF: Single arm, open-label study to provide Defibrotide to patients diagnosed with VOD. Defibrotide is no longer available though the Emergency Use IND mechanism (also known as compassionate use, or single patient named use). This protocol is the only mechanism by which Defibrotide can be made available to patients in the U.S. ; DRUG USED: Defitelio; DRUG CLASS: New Molecular Entity (NME); INDICATION: Sinusoidal Obstruction Syndrome (Veno-Occlusive Disease / VOD); TARGET: Eicosanoids; THERAPY: Monotherapy; LEAD SPONSOR: Jazz Pharmaceuticals; CRITERIA: Inclusion Criteria: Entry criteria include the following: 1. Clinical diagnosis of VOD, made by Baltimore Criteria, Modified Seattle Criteria, or biopsy proven: 1.1 Baltimore Criteria- Bilirubin ≥2 mg/dL and at least 2 of the following clinical findings: - Ascites (radiographic or physical exam) - Weight gain of ≥5% compared to the day of conditioning-- if this value is not available, the weight on the date of admission to the SCT unit may be used) - Hepatomegaly; increased over baseline. 1.2 Modified Seattle Criteria: At least two of the following - Bilirubin ≥2 mg/dL - Ascites (radiographic or physical exam) and/or weight gain ≥5% above baseline weight (defined as weight on the first day of conditioning- if this value is not available, the weight on the date of admission to the SCT unit may be used) - hepatomegaly increased over baseline 1.3 Patients that do not meet the Baltimore Criteria or Modified Seattle Criteria and have biopsy proven VOD are eligible. 2. Patient must also provide written informed consent. Exclusion Criteria: - Use of any medication which increases the risk of hemorrhage is disallowed. Use of heparin or other anticoagulants is disallowed within 12 hours unless being used for routine central venous line management, fibrinolytic instillation for central venous line occlusion, intermittent dialysis or ultrafiltration of CVVH. - Clinically significant uncontrolled acute bleeding, defined as hemorrhage requiring > 15 cc/kg of packed red blood cells (e.g., a pediatric patient weighing 20 kg and requiring > 300cc of packed red blood cells/24 hours, or an adult patient weighing 70 kg and requiring >3 units of packed red blood cells/24 hours) to replace blood loss, OR bleeding from a site which in the Investigators opinion constitutes a potential life-threatening source (e.g. pulmonary hemorrhage or CNS bleeding), irrespective of amount of blood loss, at any point from the date of SCT through the date of severe VOD diagnosis. - Hemodynamic instability as defined by a requirement for multiple pressors, or inability to maintain mean arterial pressure (for children: to maintain mean arterial pressure within 1 standard deviation of age-adjusted levels) with single pressor support. - Woman who are pregnant. ; PRIMARY OUTCOME: Survival by Day+100 Post Stem Cell Transplant or Chemotherapy; SECONDARY OUTCOME 1: "
# should be Yes
pipe = transformers.pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=100)
result = pipe(f"<s>[INST]<<SYS>> {sys} <</SYS>> {prompt} [/INST]")
generated_text = result[0]['generated_text']
print(generated_text)