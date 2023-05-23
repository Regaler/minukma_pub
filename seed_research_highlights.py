"""
This script seeds the initial data to the ResearchHighlight table.
"""
from app import app, db
from models import ResearchHighlight

research_highlights_data = [
    {
        'image': "/static/research0.PNG",
        'alt': "Research Project 0",
        'link': "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9177249/",
        'title': "Artificial intelligence–powered spatial analysis of tumor-infiltrating lymphocytes as complementary biomarker for immune checkpoint inhibition in non–small-cell lung cancer, JCO 2022",
        'description': "Biomarkers on the basis of tumor-infiltrating lymphocytes (TIL) are potentially valuable in predicting the effectiveness of immune checkpoint inhibitors (ICI). However, clinical application remains challenging because of methodologic limitations and laborious process involved in spatial analysis of TIL distribution in whole-slide images (WSI)."
    },
    {
        'image': "/static/research1.PNG",
        'alt': "Research Project 1",
        'link': "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=vWZH2LoAAAAJ&citation_for_view=vWZH2LoAAAAJ:9yKSN-GCB0IC",
        'title': "Artificial intelligence–powered programmed death ligand 1 analyser reduces interobserver variation in tumour proportion score for non–small cell lung cancer with better prediction of immunotherapy response, EJC 2022",
        'description': "This study explored the role of artificial intelligence (AI)-powered TPS analyser in minimisation of interobserver variation and enhancement of therapeutic response prediction."
    },
    {
        'image': "/static/research2.jpg",
        'alt': "Research Project 2",
        'link': "https://www.e-crt.org/journal/view.php?number=3400",
        'title': "Diagnostic Assessment of Deep Learning Algorithms for Frozen Tissue Section Analysis in Women with Breast Cancer",
        'description': "Assessing the metastasis status of the sentinel lymph nodes (SLNs) for hematoxylin and eosin–stained frozen tissue sections by pathologists is an essential but tedious and time-consuming task that contributes to accurate breast cancer staging. This study aimed to review a challenge competition (HeLP 2019) for the development of automated solutions for classifying the metastasis status of breast cancer patients."
    },
    {
        'image': "/static/research3.PNG",
        'alt': "Research Project 3",
        'link': "https://openaccess.thecvf.com/content_CVPR_2019/papers/Kim_Progressive_Attention_Memory_Network_for_Movie_Story_Question_Answering_CVPR_2019_paper.pdf",
        'title': "Progressive attention memory network for movie story question answering, CVPR 2019",
        'description': "This paper proposes the progressive attention memory network (PAMN) for movie story question answering (QA). Movie story QA is challenging compared to VQA in two aspects:(1) pinpointing the temporal parts relevant to answer the question is difficult as the movies are typically longer than an hour,(2) it has both video and subtitle where different questions require different modality to infer the answer. To overcome these challenges, PAMN involves three main features:(1) progressive attention mechanism that utilizes cues from both question and answer to progressively prune out irrelevant temporal parts in memory,(2) dynamic modality fusion that adaptively determines the contribution of each modality for answering the current question, and (3) belief correction answering scheme that successively corrects the prediction score on each candidate answer. Experiments on publicly available benchmark datasets, MovieQA and TVQA, demonstrate that each feature contributes to our movie story QA architecture, PAMN, and improves performance to achieve the state-of-the-art result. Qualitative analysis by visualizing the inference mechanism of PAMN is also provided."
    },
    {
        'image': "/static/research4.PNG",
        'alt': "Research Project 4",
        'link': "https://openaccess.thecvf.com/content_CVPR_2020/papers/Kim_Modality_Shifting_Attention_Network_for_Multi-Modal_Video_Question_Answering_CVPR_2020_paper.pdf",
        'title': "Modality shifting attention network for multi-modal video question answering, CVPR 2020",
        'description': "This paper considers a network referred to as Modality Shifting Attention Network (MSAN) for Multimodal Video Question Answering (MVQA) task. MSAN decomposes the task into two sub-tasks:(1) localization of temporal moment relevant to the question, and (2) accurate prediction of the answer based on the localized moment. The modality required for temporal localization may be different from that for answer prediction, and this ability to shift modality is essential for performing the task. To this end, MSAN is based on (1) the moment proposal network (MPN) that attempts to locate the most appropriate temporal moment from each of the modalities, and also on (2) the heterogeneous reasoning network (HRN) that predicts the answer using an attention mechanism on both modalities. MSAN is able to place importance weight on the two modalities for each sub-task using a component referred to as Modality Importance Modulation (MIM). Experimental results show that MSAN outperforms previous state-of-the-art by achieving 71.13% test accuracy on TVQA benchmark dataset. Extensive ablation studies and qualitative analysis are conducted to validate various components of the network."
    },
    {
        'image': "/static/research5.PNG",
        'alt': "Research Project 5",
        'link': "https://arxiv.org/pdf/2008.10238.pdf",
        'title': "Gaining Extra Supervision via Multi-task learning for Multi-Modal Video Question Answering, IJCNN 2020",
        'description': "This paper proposes a method to gain extra supervision via multi-task learning for multi-modal video question answering. Multi-modal video question answering is an important task that aims at the joint understanding of vision and language. However, establishing large scale dataset for multi-modal video question answering is expensive and the existing benchmarks are relatively small to provide sufficient supervision. To overcome this challenge, this paper proposes a multi-task learning method which is composed of three main components: (1) multi-modal video question answering network that answers the question based on the both video and subtitle feature, (2) temporal retrieval network that predicts the time in the video clip where the question was generated from and (3) modality alignment network that solves metric learning problem to find correct association of video and subtitle modalities. By …"
    },
]

def seed_research_highlights():
    for highlight_data in research_highlights_data:
        highlight = ResearchHighlight(**highlight_data)
        db.session.add(highlight)

    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_research_highlights()
