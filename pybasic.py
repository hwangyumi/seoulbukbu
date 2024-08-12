import streamlit as st
import random

def gugudan():
    dan=st.number_input("구구단 몇단으로 할까요?",value=0)
    if dan>1:
        for i in range(1,10):
            r=dan*i
            st.write(f"{dan}*{i}= {r}")

# 음식추천 프로그램

def recommand_food():
    c_food=['짜장면','짬뽕','탕수육','팔보채','유산슬']
    k_food=['김밥','설렁탕','갈비','삼겹살','백반']
    menu=st.radio("음식추천",["한식","중식"],index=None)
    if menu=="중식":
        st.write(f"오늘의 중식 추천메뉴:{random.choice(c_food)}")
    if menu=="한식":
        st.write(f"오늘의 한식 추천메뉴:{random.choice(k_food)}")
    else:
        st.write("음식종류를 선택하세요")



def basic():
    tab1, tab2 = st.tabs(["구구단", "음식추천"])

    with tab1:
        gugudan()
    with tab2:
        recommand_food()
