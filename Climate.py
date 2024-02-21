import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title('Climate Action Dashboard')

def scrape_news():
    url = "https://www.sciencedaily.com/news/earth_climate/climate/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('h3', class_='latest-head')
    news_list = []
    for article in articles:
        news_list.append(article.text.strip())
    return news_list


latest_news = scrape_news()
for news in latest_news:
    st.write(news)

climate_updates_content = "For comprehensive climate change reports and updates, visit [UN Climate Change Reports](https://www.un.org/en/climatechange/reports)"

st.markdown(climate_updates_content)

navigation_links = {
    "Latest News": "Link to the latest news goes here.",
    "Climate Updates": climate_updates_content,
    "Articles": "Summarize key findings from IPCC and IEA reports in digestible formats. For detailed articles, please visit [National Geographic Climate Change](https://education.nationalgeographic.org/resource/climate-change/)",
    "Infographics & Videos": "Include placeholder elements for infographics and videos. Later, embed actual graphics or link to relevant [YouTube videos](https://www.youtube.com/watch?v=0kVMhvDClII) explaining complex concepts visually.",
    "Survey": "",
    "Renewable Energy Explorer": "Four key climate change indicators - greenhouse gas concentrations, sea level rise, ocean heat and ocean acidification...",
    "Energy Efficiency Guide": "Energy efficiency is a simple, quick and cost-effective method to reduce both costs and greenhouse gas (GHG) emissions...",
    "Success Story Gallery": "Showcase real-world examples of individuals and communities adopting renewable energy and energy efficiency measures.",
    "Interactive Tools": "",
    "Action Platform": "Connect with Providers Section: Create a searchable directory of local installers, suppliers, and financing options for renewable energy solutions."
}

selected_section = st.sidebar.radio("Navigate", list(navigation_links.keys()))

st.header(selected_section)

if selected_section == "Infographics & Videos":
    # Embed YouTube video
    st.video("https://www.youtube.com/watch?v=NZDUOPyQ0Rs")

else:
    # Display text content for other sections
    st.markdown(navigation_links[selected_section])

if selected_section == "Energy Efficiency Guide":
    st.button("Calculate Savings")

elif selected_section == "Action Platform":
    st.button("Shop Now")
    st.button("Make a Pledge")
