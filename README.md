# SS.LV notification script

Problem: The Latvian advertisements platform ss.lv doesn't have a notification feature what requires to check the desired product's page again and again. The problem is that you waste a lot of time on it, moreover, often you forget to do it thereby losing potential deals.
<br><br>
Solution: A web scraper build in Python that runs automatically through Windows Task Scheduler (or any other similar program). When a change on the page satisfies your criteria, the script sends you an email notifying you that the product is available.
<br><br>
Example: I want to buy an old, rare car (criteria: year<2000) that appears in advertisements not so often. The demand is high, therefore, I must check the page every 3 hours. Instead of doing it I run this web_scraper.py script using Task Scheduler every n hours. When the car is available, I get a notification on my email.
<br><br>
Possibilities for development: If needed it's possible to create a user interface where a client could choose necessary categories (cars/real estate/tickets to events e.t.c) and criteria (price, date of issue, location) in doing so making product monitoring easier.
