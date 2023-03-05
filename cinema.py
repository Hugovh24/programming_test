from bs4 import BeautifulSoup
import pandas as pd
import requests

def transform(url):
    # Recover HTML code
    request = requests.get(url)
    soup = BeautifulSoup(request.content, "html.parser")

    # Allow to recover title and year for each movie
    title_and_year = soup.findAll('div', attrs={'class': "item-name"})
    list_title_and_date = [title_and_year[i].text.strip().replace(")", "").split(" (") for i in range(len(title_and_year))]

    # Allow to recover the number of votes for each movie
    down_votes = soup.find_all("span", attrs={"class", "listVote-downVoteCount"})
    up_votes = soup.find_all("span", attrs={"class", "listVote-upVoteCount"})
    number_votes = [int(down_votes[i].text) + int(up_votes[i].text) for i in range(len(down_votes))]

    # DataFrame construction
    res = pd.DataFrame(list_title_and_date, columns=["title", "year"])
    res['ranking'] = range(1, len(list_title_and_date) + 1)
    res["no_of_votes"] = number_votes

    return res.to_csv()

# URL of the page you want to parse, here: 100 Must See Movies for More Advanced Cinephiles
url_to_recover = "https://www.listchallenges.com/100-must-see-movies-for-more-advanced-cinephiles/vote"

# Call transform method to recover movies data in CSV
data = transform(url_to_recover)
