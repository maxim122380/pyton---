import requests

token = "vk1.a.8XI2_UyJ57mJItBtvbKS7AOSk5egx-DvBip_6dPi4p4sl9snZovZn_GqYmmUr3XkdD-0iN8CHgoGd_E3UJ1z7JjnSsRQ8MUizsjHf_O7nHTkqx2ntx77bXhoesmLFpbjghRNjSgTmJX_BnH7DdEp0B-DryICnt5kfZZXMlucqDBDMB6WPoDuOJeIWHPK8X42PFu6vnsxa61oLdInDDwB5A"
version = 5.199

def get_param(link):
    return link[link.find("wall") + 4:].split("_")

class Vkconnect:
    def __init__(self, version, token):
        self.version = version
        self.token = token
        self.url = f"https://api.vk.com/method/"

    def profileinfo(self):
        return requests.get(
            f"{self.url}account.getProfileInfo?access_token={self.token}&v={self.version}").json()
    
    def like(self, type, link):
        if type == "post":
            param = get_param(link)
            item_id, owner_id = param[1], param[0]
            return requests.get(f"{self.url}likes.add?access_token={self.token}&v={self.version}&type={type}&item_id={item_id}&owner_id={owner_id}").json()
        else:
            return "Ссылка идёт не на пост"
        
    def banned(self):
        return requests.get(f"{self.url}account.getBanned?access_token={self.token}&v={self.version}").json()
    
    def ban(self, owner_id):
        return requests.get(f"{self.url}account.ban?access_token={self.token}&v={self.version}&owner_id={owner_id}").json()
    
    def unban(self, owner_id):
        return requests.get(f"{self.url}account.unban?access_token={self.token}&v={self.version}&owner_id={owner_id}").json()
        
vk = Vkconnect(version, token)
print(vk.like("post", "https://vk.com/wall-206722684_321"))

"""
vk = Vkconnect(version, token)
print(vk.profileinfo())

vk = Vkconnect(version, token)
print(vk.banned())

vk = Vkconnect(version, token)
print(vk.ban("466938825"))

vk = Vkconnect(version, token)print(vk.unban("466938825"))

"""


