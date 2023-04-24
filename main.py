import streamlit as st

# Add a video
video_file = open('output_Full.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

# Add some text
#st.write("This is some example text.")
# Add a horizontal line
st.markdown("<hr>", unsafe_allow_html=True)
# Add formatted text
st.markdown("## Questions and Answers")
#st.markdown("This is some *formatted* text.")

# Add a container with a border style
# container_style = """
#     border: 2px solid black;
#     padding: 10px;
# """
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("Is the mass of the gray cube greater than twice of the mass of the brown cube?\nA. No.\nB. Can not answer.\nC. Yes.")
    st.markdown("A")
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("Which of the following statements is true regarding the mass of the gray cube and the brown cube?\nA. It is impossible to determine the relationship between the masses of the gray cube and the brown cube based on the information given.\nB. The mass of the gray cube is not greater than twice of the mass of the brown cube.\nC. The mass of the gray cube is greater than twice of the mass of the brown cube.")
    st.markdown("B")
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("Which statement is true about the mass of the gray cube and the brown cube?\nA. The mass of the gray cube is not greater than twice of the mass of the brown cube.\nB. The mass of the gray cube is greater than twice of the mass of the brown cube.\nC. It is impossible to determine the relationship between the masses of the gray cube and the brown cube based on the information given.")
    st.markdown("A")
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("Which statement accurately compares the mass of the gray cube to that of the brown cube?\nA. The mass of the gray cube is greater than twice of the mass of the brown cube.\nB. The mass of the gray cube is not greater than twice of the mass of the brown cube.\nC. It is impossible to determine the relationship between the masses of the gray cube and the brown cube based on the information given.")
    st.markdown("B")
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("The mass of the gray cube is represented by 'x' and the mass of the brown cube is represented by 'y'. Which of the following inequalities represents the relationship between the mass of the gray cube and twice of the mass of the brown cube?\nA. x > 2y.\nB. x = 2y.\nC. x < 2y.")
    st.markdown("B")
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("Which object in the following options has the maximum mass?\nA. The red cube.\nB. The blue sphere.\nC. The yellow cube.")
    st.markdown("C")
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("Which object in the following options has the minimum mass?\nA. The red cube.\nB. The blue sphere.\nC. The yellow cube.")
    st.markdown("A")
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("How many fixed points are there in the video?")
    st.markdown("10")
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("How many yellow objects are there in the video?")
    st.markdown("15")
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("Is there any magenta triple-rod pulley in the video?")
    st.markdown("no")
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("Is the average tension of the pink rope greater than twice of the average tension of the white rope?\nA. No.\nB. Can not answer.\nC. Yes.")
    st.markdown("C")
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("Which of the following statements is true regarding the average tension of the pink rope and the white rope?\nA. The average tension of the pink rope is not greater than twice of the average tension of the white rope.\nB. It is impossible to determine the relationship between the average tension of the pink rope and the white rope based on the information given.\nC. The average tension of the pink rope is greater than twice of the average tension of the white rope.")
    st.markdown("C")
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("Which statement is true about the average tension of the pink rope and the white rope?\nA. It is impossible to determine the relationship between the average tension of the pink rope and the white rope based on the information given.\nB. The average tension of the pink rope is not greater than twice of the average tension of the white rope.\nC. The average tension of the pink rope is greater than twice of the average tension of the white rope.")
    st.markdown("C")
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("Which statement accurately compares the average tension of the pink rope to that of the white rope?\nA. The average tension of the pink rope is not greater than twice of the average tension of the white rope.\nB. It is impossible to determine the relationship between the average tension of the pink rope and the white rope based on the information given.\nC. The average tension of the pink rope is greater than twice of the average tension of the white rope.")
    st.markdown("C")
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("The average tension of the pink rope is represented by 'x' and the average tension of the white rope is represented by 'y'. Which of the following inequalities represents the relationship between the average tension of the pink rope and twice of the average tension of the white rope?\nA. x = 2y.\nB. x < 2y.\nC. x > 2y.")
    st.markdown("C")
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.write("Which rope in the following options has the maximum average tension?\nA. The pink rope.\nB. The white rope.\nC. The black rope.")
    st.markdown("B")
