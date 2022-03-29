test_list  = ['<script\x20type="text/javascript">console.log("test success...")</script>', 
    '<script\x3Etype="text/javascript">console.log("test success...")</script>',
    '<script\x0Dtype="text/javascript">console.log("test success...")</script>',
    '<script\x09type="text/javascript">console.log("test success...")</script>',
    '<script\x0Ctype="text/javascript">console.log("test success...")</script>',
    '<script\x2Ftype="text/javascript">console.log("test success...")</script>',
    '<script\x0Atype="text/javascript">console.log("test success...")</script>']

  
# initializing string 
test_str = '<'
  
# printing original list
print("The original list is : " + str(test_list))
  
# Remove List elements containing String character
# Using loop
res = []
for sub in test_list:
    flag = 0
    for ele in sub:
        if ele in test_str:
            flag = 1
    if not flag:
        res.append(sub)
  
# printing result 
print("The list after removal : " + str(res))