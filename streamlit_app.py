# Credit: This app is inspired by https://huggingface.co/spaces/osanseviero/esmfold

import streamlit as st
from stmol import showmol
import py3Dmol
import requests
import tempfile

#st.set_page_config(layout = 'wide')
st.title('🎈 ESMfold')

# stmol
def render_mol(pdb):
    pdbview = py3Dmol.view()
    pdbview.addModel(pdb,'pdb')
    pdbview.setStyle({'cartoon':{'color':'spectrum'}})
    pdbview.setBackgroundColor('white')#('0xeeeeee')
    pdbview.zoomTo()
    pdbview.zoom(2, 800)
    showmol(pdbview, height = 500,width=800)

# ESMfold
DEFAULT_SEQ = "MGSSHHHHHHSSGLVPRGSHMRGPNPTAASLEASAGPFTVRSFTVSRPSGYGAGTVYYPTNAGGTVGAIAIVPGYTARQSSIKWWGPRLASHGFVVITIDTNSTLDQPSSRSSQQMAALRQVASLNGTSSSPIYGKVDTARMGVMGWSMGGGGSLISAANNPSLKAAAPQAPWDSSTNFSSVTVPTLIFACENDSIAPVNSSALPIYDSMSRNAKQFLEINGGSHSCANSGNSNQALIGKKGVAWMKRFMDNDTRYSTFACENPNSTRVSDFRTANCSLEDPAANKARKEAELAAATAEQ"
txt = st.text_area('Input sequence', DEFAULT_SEQ)

c = st.empty()

def update(sequence=txt):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence)
    name = sequence[:3] + sequence[-3:] 
    pdb_string = response.content.decode('utf-8')
    return c.write(render_mol(pdb_string))

st.button('Predict', on_click=update)

#uploaded_file = st.sidebar.file_uploader('Upload PDB file')

##showmol(render_pdb(id = '3EQM'))

#if uploaded_file is not None:
#  showmol(obj_upload(uploaded_file).setStyle({'cartoon':{'color':'spectrum'}}) )
#else:
#  st.info('Awaiting input ...')
