import streamlit as st
import os

import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Float, Date




st.write('''
# Understanding the Venezuelan Crisis
## Analysis of 20 years of news articles. 
''')

st.markdown(
    """
 <style>
.stApp {
  background-image: url("https://images.unsplash.com/photo-1621622633934-b910be06148d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3538&q=80,%s");
  background-size: cover;
}
</style>
    """,
    unsafe_allow_html=True
)

st.write(''' 
       #### Choose one of the following times frames to see the main topics in the news
''')



period  = st.selectbox(
     'Select one period',
     ('1999-2004', '2004-2009', '2009-2014', '2014-2017', '2017-2021', 'Up to December 2021'))


if (period == '1999-2004') :
    st.write('''
    The main topics in this time frame were:
    
    * Topic 1: [oil company](https://www.theguardian.com/world/2002/apr/08/venezuela.oil),
    president hugo,
    [general strike](https://www.theguardian.com/world/2002/dec/07/oil.venezuela),
    [state oil](https://www.theguardian.com/world/2002/dec/28/venezuela.alexbellos)
    * Topic 2: peaceful revolution,constituent assembly,latin america,
    [new constitution](https://www.theguardian.com/world/1999/dec/17/alexbellos)
    * Topic 3: fidel castro,april fool,castro want,anti castro
    * Topic 4: qualify finals,beat uruguay,play australia,south american
    * Topic 5: pedro carmona,oil price,white house,unite state
    ''')

if period == '2004-2009' :
    st.write('''
    The main topics in this time frame were:
    
    * Topic 1: latin american, 
    [george bush](https://www.theguardian.com/news/blog/2007/mar/12/snappingatbus) 
    ,[bush administration](https://www.theguardian.com/world/2005/feb/22/venezuela.julianborger), venezuelan president
    * Topic 2: [land reform](https://www.theguardian.com/world/2005/mar/14/venezuela),
    radio television,
    [press freedom](https://www.theguardian.com/media/greenslade/2006/jul/21/pressfreedominvestigationin), president hugo
    * Topic 3: [human right](https://www.theguardian.com/world/2008/sep/18/venezuela.humanrights),
    latin american, simon bolivar, latin america
    * Topic 4: public service,[socialist revolution](https://www.theguardian.com/commentisfree/2006/may/15/chavezispopulistnotasocia),
    term limit,[opinion poll](https://www.theguardian.com/world/2004/aug/16/venezuela.danglaister)
    * Topic 5: [colombia farc](https://www.theguardian.com/world/2008/sep/13/venezuela.usa),
    revolutionary arm, force colombia, arm force
    ''')

    
    
if period == '2009-2014' :
    st.write('''
    The main topics in this time frame were:
    
    * Topic 1: president nicolas, rule party,
    [henrique capriles](https://www.theguardian.com/world/2012/feb/13/venezuela-hugo-chavez),
    national assembly
    * Topic 2: [unite state](https://www.theguardian.com/commentisfree/2013/apr/22/united-states-contempt-venezuelan-democracy),
     south america, socialist revolution, president hugo
    * Topic 3: henrique capriles,
     [south america](https://www.theguardian.com/world/2013/mar/06/south-american-leaders-venezuelans-chavez)
    , unite state, latin american
    * Topic 4: [socialist revolution](https://www.theguardian.com/world/2012/oct/08/venezuela-election-hugo-chavez),
    vice president, human right, national guard
    * Topic 5: national assembly, socialist revolution, oil revenues,
    [oil company](https://www.theguardian.com/world/2009/jul/16/venezuela-oil-hugo-chavez-politics)
    ''')
    
   

if period == '2014-2017' :
    st.write('''
    The main topics in this time frame were:
    
    * Topic 1: [nicolas maduro](https://www.theguardian.com/world/2012/dec/12/hugo-chavez-heir),
    [recall referendum](https://www.theguardian.com/world/2009/feb/16/venezuela-hugo-chavez),
    oil price,
    [national assembly](https://www.theguardian.com/world/2010/sep/23/hugo-chavez-venezuelan-assembly-vote)
    * Topic 2: [human right abuse](https://www.theguardian.com/commentisfree/2014/mar/06/europe-left-condemn-human-rights-violations-venezuela-chavez-maduro),
    right abuse, latin america, human right
    * Topic 3: late president hugo,late president,president hugo,president hugo chavez
    * Topic 4: [price control](https://www.theguardian.com/world/2013/nov/11/venezuela-troops-patrol-stores-control-inflation), 
     currency control, exchange rate,
    [black market](https://www.theguardian.com/global-development-professionals-network/2015/apr/16/venezuela-economy-black-market-milk-and-toilet-paper)
    * Topic 5: [leader leopoldo](https://www.theguardian.com/world/2015/sep/11/venezuela-opposition-leader-leopoldo-lopez-sentenced-to-14-years-in-jai),
     leader leopoldo lopez,
    [opposition leader](https://www.theguardian.com/world/2013/apr/25/venezuela-threatens-opposition-leader-protest),leopoldo lopez
    ''')
    
if period == '2017-2021' :
    st.write('''
    The main topics in this time frame were:
    
    * Topic 1: nicolas maduro,
    [opposition leader](https://www.theguardian.com/world/2019/feb/05/maduro-veiled-threat-jail-venezuela-opposition-leader-juan-guaido),
    [donald trump](https://www.theguardian.com/commentisfree/2019/jan/24/donald-trump-venezuela-nicolas-maduro),
    juan guaido
    * Topic 2: [work class family](https://www.theguardian.com/world/2018/feb/12/venezuelan-middle-class-economic-crisis-pawn-shops),
    [human right](https://www.theguardian.com/world/2019/oct/17/venezuela-un-human-rights-council-activists-outraged),
    [sanction maduro](https://www.theguardian.com/world/2019/jan/28/trump-venezuela-sanctions-oil-pdvsa-maduro-guaido),
    [oil price](https://www.theguardian.com/business/2018/oct/12/oil-price-barrel-markets-iran-sanctions)
    * Topic 3: import food medicine,[electoral boycott](https://www.theguardian.com/world/2017/dec/08/venezuela-opposition-boycott-mayoral-elections),
    import food,black market
    * Topic 4: brief deliver thousands,sign morning,sign morning brief,morning brief
    * Topic 5: [supreme court](https://www.theguardian.com/world/2017/jun/28/venezuela-supreme-court-grenade-police-helicopter),
    [security force](https://www.theguardian.com/world/2017/jun/20/venezuela-protester-killed-demonstrations),
    [human right](https://www.theguardian.com/world/2020/sep/16/venezuela-un-report-crimes-against-humanity-maduro-government),
    [constituent assembly](https://www.theguardian.com/world/2017/jul/29/venezuela-government-maduro-vote-end-democracy)
    
    ''')

    
    
if period == 'Up to December 2021' :
    st.write(''' 
    The main topics in this time frame were:
    
    * Topic 1: [venezuelan refugees](https://www.theguardian.com/global-development/2021/jul/06/i-didnt-eat-for-days-hunger-stalks-venezuelan-refugees),
    human right,latin american,[latin america](https://www.theguardian.com/global-development/2021/jun/21/latin-america-will-never-be-the-same-venezuela-exodus-reaches-record-levels)
    * Topic 2: [refugees migrants](https://www.theguardian.com/global-development/2021/feb/11/i-can-build-a-real-life-colombia-to-grant-legal-status-to-venezuelan-migrants),drug traffic,tell guardian,year old
    * Topic 3: president nicolas,[president nicolas maduro](https://www.theguardian.com/world/2021/jan/18/venezuela-nicolas-maduro-oxygen-brazil-covid),
    drug traffic, nicolas maduro
    * Topic 4: president nicolas maduro, president nicolas, nicolas maduro, political crisis
    * Topic 5: economic social,refugee agency, venezuelan migrants, million venezuelans
    ''')

    
    
 ##Database connection for user generated queries.

st.markdown("""<hr style="height:10px;border:none;color:##E8E8E8;background-color:##E8E8E8	;" /> """, unsafe_allow_html=True)
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.write("## Now, you will have the chance to explore articles on your own")

st.write("### You can try your own words to search")
word = st.text_input('Type here')
st.write("Write a year (from 1999 to present times)")
year = st.number_input(label=' ',min_value=1999, max_value=2021)
num_art = st.slider('How many articles would you like to check?', 1, 7, 1)

engine = create_engine('sqlite:///newsve.db', echo=False)
# articles = pd.read_sql_query(f"SELECT title, url FROM newstable limit {num_art}", engine)
# st.write("Articles: ", articles)

rows = engine.execute(f"SELECT title, url, date FROM news_table WHERE title LIKE COLLATE Latin1_general_CI_AI '%{word}%' AND date LIKE '%{year}%' LIMIT {num_art}").fetchall()

st.markdown("""<hr style="height:10px;border:none;color:#696969;background-color:#333;" /> """, unsafe_allow_html=True)

# Print results.
st.write(f"### Results for the search of '{word}' in the year {year}")

#If there are articles to show
if rows:
    for row in rows:
        st.write(f"Title : {row[0]}")
        st.write(f"{row[1]}")
        
else:
    st.write("Sorry, there are no articles to show for this search")
# def header(url):
#      st.markdown(f'<p style="background-color:rgba(255, 255, 255, 0.5);opacity: 0.5;color:#000000;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        
# header('Test')
