import requests, unittest

class TestFind(unittest.TestCase):
    def testFindAllTeacher(self):
        # 准备数据
        url = "http://www.jasonisoft.cn:8080/HKR/TeacherServlet?method=findAllTeacher"
        data = {

        }
        expect = 200

        # 调用被测接口
        response = requests.post(url=url, data=data)
        response.encoding = "utf-8"

        code = response.status_code
        txt = response.text

        # 断言
        print(txt)
        self.assertEqual(expect, code)

    def testFindAllStudent(self):
        # 准备数据
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllStudent"
        data = {

        }
        expect = 200

        # 调用被测接口
        response = requests.post(url=url, data=data)
        response.encoding = "utf-8"

        code = response.status_code
        txt = response.text

        # 断言
        print(txt)
        self.assertEqual(expect, code)

    def testFindAllCourse(self):
        # 准备数据
        url = "http://www.jasonisoft.cn:8080/HKR/CourseServlet?method=findAllCourse"
        data = {

        }
        expect = 200

        # 调用被测接口
        response = requests.post(url=url, data=data)
        response.encoding = "utf-8"

        code = response.status_code
        txt = response.text

        # 断言
        print(txt)
        self.assertEqual(expect, code)



    def testFindAllLog(self):
        # 准备数据
        url = "http://www.jasonisoft.cn:8080/HKR/LogServlet?method=findAllLog"
        data = {

        }
        expect = 200

        # 调用被测接口
        response = requests.post(url=url, data=data)
        response.encoding = "utf-8"

        code = response.status_code
        txt = response.text

        # 断言
        print(txt)
        self.assertEqual(expect, code)

    def testGetTodayAllEvaluate(self):
        # 准备数据
        url = "http://www.jasonisoft.cn:8080/HKR/EvaluateServlet?method=getTodayAllEvaluate"
        data = {

        }
        expect = 200
        # 调用被测接口
        response = requests.post(url=url, data=data)
        response.encoding = "utf-8"
        code = response.status_code
        txt = response.text
        # 断言
        print(txt)
        self.assertEqual(expect, code)

    def testFindByDate(self):
        # 准备数据
        url = "http://www.jasonisoft.cn:8080/HKR/LogServlet?method=findByDate"
        data = {

        }
        expect = 200
        # 调用被测接口
        response = requests.post(url=url, data=data)
        response.encoding = "utf-8"
        code = response.status_code
        txt = response.text
        # 断言
        print(txt)
        self.assertEqual(expect, code)

    def testGetByDate(self):
        # 准备数据
        url = "http://www.jasonisoft.cn:8080/HKR/EvaluateServlet?method=getByDate"
        data = {

        }
        expect = 200
        # 调用被测接口
        response = requests.post(url=url, data=data)
        response.encoding = "utf-8"
        code = response.status_code
        txt = response.text
        # 断言
        print(txt)
        self.assertEqual(expect, code)

    def testFindByUsernameAndPhone(self):
        # 准备数据
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findByUsernameAndPhone"
        data = {
            "phoneNumber": " ",
            "username": " "
        }
        expect = 500
        # 调用被测接口
        response = requests.post(url=url, data=data)
        response.encoding = "utf-8"
        code = response.status_code
        txt = response.text
        # 断言
        print(txt)
        self.assertEqual(expect, code)

    def testFindByUsername(self):
        # 准备数据
        url = "http://www.jasonisoft.cn:8080/HKR/TeacherServlet?method=findByUsername"
        data = {

        }
        expect = 200
        # 调用被测接口
        response = requests.post(url=url, data=data)
        response.encoding = "utf-8"
        code = response.status_code
        txt = response.text
        # 断言
        print(txt)
        self.assertEqual(expect, code)