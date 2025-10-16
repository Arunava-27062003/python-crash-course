name = "arunAva kuNdu"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "rahul"
last_name = "biswas"

full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

str_with_whitespace=" Itadori   "
print(str_with_whitespace)
print(str_with_whitespace.strip()) # remove whitespace from both left and right
print(str_with_whitespace.rstrip()) # remove whitespace from right only

site_url="https://www.example.com"
mod_url=site_url.removeprefix("https://")
print(mod_url)