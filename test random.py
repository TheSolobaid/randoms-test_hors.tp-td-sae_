from urllib.request import Request, urlopen

class AnalyseurWeb:
    def __check_machine_name(url) -> bool :
        

    def open_url(self, machine_name):
        isopen = False
        isopen = self.__check_machine_name(machine_name)
        if isopen :
            sock = urlopen(url)
            AnalyseurWeb.historique(url)
            page = sock.read()
            sock.close()
            return page.decode("utf-8")
        else :
            return ""