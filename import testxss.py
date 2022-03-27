import testxss
from concurrent.futures import ProcessPoolExecutor

scan = testxss.scan_xss

List = ['<script\x20type="text/javascript">console.log("test success...")</script>', 
    '<script\x3Etype="text/javascript">console.log("test success...")</script>',
    '<script\x0Dtype="text/javascript">console.log("test success...")</script>',
    '<script\x09type="text/javascript">console.log("test success...")</script>',
    '<script\x0Ctype="text/javascript">console.log("test success...")</script>',
    '<script\x2Ftype="text/javascript">console.log("test success...")</script>',
    '<script\x0Atype="text/javascript">console.log("test success...")</script>']

with ProcessPoolExecutor(max_workers = 3) as executor:
    result = executor.map(scan, List)

print([x for x in result])

