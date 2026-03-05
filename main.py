from dataclasses import dataclass

#4
@dataclass
class Profil:
    username: str
    email: str
    parol: str
    oxirgi_kirish: int

    def parolni_tekshir(self):
        return len(self.parol) == 8
