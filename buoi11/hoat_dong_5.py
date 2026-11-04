import requests


print("--- Bài tập 5.1: API GitHub ---")
url_github = "https://api.github.com/repos/python/cpython"
response_gh = requests.get(url_github)

if response_gh.status_code == 200:
    du_lieu = response_gh.json()
    print("Ten repository:", du_lieu["full_name"])
    print("So luot gan sao (stars):", du_lieu["stargazers_count"])
    print("Ngon ngu chinh:", du_lieu["language"])
else:
    print("Goi API that bai, ma loi:", response_gh.status_code)

print("\n" + "="*40 + "\n")


print("--- Bài tập 5.2: API Tỷ giá ngoại tệ ---")
url_rates = "https://open.er-api.com/v6/latest/USD"
response_rate = requests.get(url_rates)

if response_rate.status_code == 200:
    du_lieu = response_rate.json()
    ty_gia_vnd = du_lieu["rates"]["VND"]
    print(f"1 USD = {ty_gia_vnd:,.0f} VND")
else:
    print("Khong lay duoc ty gia, ma loi:", response_rate.status_code)