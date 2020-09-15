# __author__:"Ming Luo"
# date:2020/9/14
import aa
aa.test_age()  # >>>  -----test_age-----
# 现在修改aa模块中的内容重复，导入模块
import aa
aa.test_age()  # >>>  -----test_age-----
# 由于python不会重复导入模块，故修改的内容没有生效
from imp import reload
reload(aa)
aa.test_age()  # >>>  -----test_age12sadsads32-----
