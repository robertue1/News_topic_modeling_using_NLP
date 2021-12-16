import streamlit as st
import os

import matplotlib.pyplot as plt
import pandas as pd





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
     'Choose one of the following time frames',
     ('1999-2004', '2004-2009', '2009-2014', '2014-2017'))

st.write('                  ')

if period == '1999-2004':
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

if period == '2004-2009':
    st.write('''
    The main topics in this time frame were:
    
    * Topic 1: latin american, 
    [george bush](https://www.theguardian.com/news/blog/2007/mar/12/snappingatbus) 
    ,[bush administration](https://www.theguardian.com/world/2005/feb/22/venezuela.julianborger),venezuelan president
    * Topic 2: [land reform](https://www.theguardian.com/world/2005/mar/14/venezuela),
    radio television,
    [press freedom](https://www.theguardian.com/media/greenslade/2006/jul/21/pressfreedominvestigationin),president hugo
    * Topic 3: [human right](https://www.theguardian.com/world/2008/sep/18/venezuela.humanrights),
    latin american,simon bolivar,latin america
    * Topic 4: public service,[socialist revolution](https://www.theguardian.com/commentisfree/2006/may/15/chavezispopulistnotasocia),
    term limit,[opinion poll](https://www.theguardian.com/world/2004/aug/16/venezuela.danglaister)
    * Topic 5: [colombia farc](https://www.theguardian.com/world/2008/sep/13/venezuela.usa),
    revolutionary arm,force colombia,arm force
    ''')

    
    
if period == '2009-2014':
    st.write('''
    The main topics in this time frame were:
    
    * Topic 1: president nicolas,rule party,
    [henrique capriles](https://www.theguardian.com/world/2012/feb/13/venezuela-hugo-chavez),
    national assembly,nicolas maduro
    * Topic 2: latin american,
    [unite state](https://www.theguardian.com/commentisfree/2013/apr/22/united-states-contempt-venezuelan-democracy),
    south america,socialist revolution,president hugo
    * Topic 3: henrique capriles,
    [south america](https://www.theguardian.com/world/2013/mar/06/south-american-leaders-venezuelans-chavez)
    ,unite state,latin american,latin america
    * Topic 4: [socialist revolution](https://www.theguardian.com/world/2012/oct/08/venezuela-election-hugo-chavez),
    vice president,national assembly,human right,national guard
    * Topic 5: national assembly,south america,socialist revolution,oil revenues,
    [oil company](https://www.theguardian.com/world/2009/jul/16/venezuela-oil-hugo-chavez-politics)
    ''')
    
   

if period == '2014-2017':
    st.write('''
    The main topics in this time frame were:
    
    * Topic 1: [nicolas maduro](https://www.theguardian.com/world/2012/dec/12/hugo-chavez-heir),
    [recall referendum](https://www.theguardian.com/world/2009/feb/16/venezuela-hugo-chavez),
    oil price,
    [national assembly](https://www.theguardian.com/world/2010/sep/23/hugo-chavez-venezuelan-assembly-vote)
    * Topic 2: [human right abuse](https://www.theguardian.com/commentisfree/2014/mar/06/europe-left-condemn-human-rights-violations-venezuela-chavez-maduro),
    right abuse,latin america,human right
    * Topic 3: late president hugo,late president,president hugo,president hugo chavez
    * Topic 4: [price control](https://www.theguardian.com/world/2013/nov/11/venezuela-troops-patrol-stores-control-inflation),
    currency control,exchange rate,
    [black market](https://www.theguardian.com/global-development-professionals-network/2015/apr/16/venezuela-economy-black-market-milk-and-toilet-paper)
    * Topic 5: [leader leopoldo](https://www.theguardian.com/world/2015/sep/11/venezuela-opposition-leader-leopoldo-lopez-sentenced-to-14-years-in-jai),
    leader leopoldo lopez,
    [opposition leader](https://www.theguardian.com/world/2013/apr/25/venezuela-threatens-opposition-leader-protest),leopoldo lopez
    ''')


    

    
# def header(url):
#      st.markdown(f'<p style="background-color:rgba(255, 255, 255, 0.5);opacity: 0.5;color:#000000;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        
# header('Test')
