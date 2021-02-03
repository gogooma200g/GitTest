from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_demo_site(self):
        # self.open("https://seleniumbase.io/demo_page.html")
        # self.open("https://www.nike.com/kr/launch/t/men/fw/nike-sportswear/DD1401-200/tcxo48/nike-dunk-hi-retro-prm")

        self.open("https://www.nike.com/kr/launch/t/women/fw/nike-sportswear/CU1450-500/dlva36/w-nike-fontanka-edge")

        self.driver.implicitly_wait(10)
        # aa = self.assert_text("COMING SOON", timeout=10)

        # print("exist ", aa)

        # 포트번호 삭제