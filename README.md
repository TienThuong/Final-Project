# Final-Project
This project is about automation testing in automationpractice.com page that I have to do 

## AutomationPractice
***Author : Bùi Tiến Thưởng - ThuongBT** 

***Project: Training Automation Test**

***Date: 23/04/2021**



                                    **Report Training automation testing**

**1. Chạy test từ dòng lệnh từng testsuite, & chạy tổng thể toàn bộ testcases để đưa ra báo cáo:**
- Chạy unittest với từng testcase, và được viết trong testsuite, các testsuite được để trong thư mục: 
		``` Final - Project\Test ```
- Chạy toàn bộ testcase bằng cách chạy file test_allsuite.py theo đường dẫn:
     ```Final-Projec\Test\test_allsuite.py```


>Output:
>
>![1](https://user-images.githubusercontent.com/83185010/116017628-5bb0f500-a66a-11eb-9f34-a688cf5adab9.png)



**2. Chạy trên 2 browsers Firefox và Chrome:**
Chạy bằng pytest, sử dụng parameterized theo các thao tác: 
   - Chạy pytest bằng cách sử dụng Teminal trong Pycharm
   - Chạy pytest đối với file test_search2 bằng câu lệnh 
      ```py.test -v -s Test\tearch_search2.py```
   >Output:
   >
   >![2brow](https://user-images.githubusercontent.com/83185010/116017695-8602b280-a66a-11eb-878b-827da71b15d6.png)

   **3. Chạy song song 2 browsers, mỗi browsers 5 testcases:**
   - Chạy pytest bằng cách sử dụng Teminal trong Pycharm
   - Chạy pytest đối với file test_search2 bằng câu lệnh 
    ```py.test -v -s -n 2 Test\test_search2.py ```
    
   >Output:
   >
   >![Screenshot_2](https://user-images.githubusercontent.com/83185010/117533717-93c81880-b018-11eb-9573-caf17fade356.png)


   **4.Setup và chạy test từ Jenkins**
   -
