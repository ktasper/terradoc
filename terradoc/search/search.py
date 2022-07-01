"""
This module deals with everything to do with searching the terraform
documentation website
"""





# def parse_docs():
#     """
#     Will search for a terraform documentation page
#     Should return a URL to the page
#     """
#     provider_doc_url = {
#     'aws': 'https://github.com/hashicorp/terraform-provider-aws/tree/main/website/docs',
#     'gcp':'AddMe'
#     }
#     doc_type = {'data':'d', 'resource':'r'}
#     url = f"{provider_doc_url['aws']}/{doc_type['data']}"
#     html_body = (requests.get(url).text)
#     soup = BeautifulSoup(html_body, "html.parser")
#     results = soup.find_all("a", class_="js-navigation-open Link--primary")
#     for i in results:
#       name = i.text
#       print (name.split('.')[0])