
import scholarly
import sys
import re

gs_search = sys.argv[1:]
gs_search = "".join(gs_search)
print(gs_search)

# get a list of google scholar results
# show them on the command line
# ask which to bibtex
# add bibtex to a predetermined file

pub_results = scholarly.search_pubs_query(gs_search)

res_list = list()
for ix in range(10):
    cur_res = next(pub_results)
    print(str(ix + 1), '\t', cur_res.bib['title'], ' - ', cur_res.bib['author'])
    res_list.append(cur_res)

indexes = input('Enter indexes to download: ')
indexes = re.split(r'\s+', indexes.strip())
indexes = list(map(int, indexes))
indexes = [i - 1 for i in indexes]

bibtex_list = list()
for ix in indexes:
    # convert to bibtex
    bib_url = res_list[ix].url_scholarbib
    pg = scholarly.scholarly._get_page(bib_url)
    bibtex_list.append(pg)

with open("culture-bibliography.bib", "a") as bib_file:
    print("\n", file = bib_file)
    print("\n".join(bibtex_list), file = bib_file)
