import numpy as np
import random
import itertools
import streamlit as st

st.title('理系でも出来るお釣り計算')
st.text("前提条件: 硬貨と紙幣の枚数は最小と仮定します")
x = st.number_input('所持金', 0,None,300)
y = st.number_input('商品価格', 0,None,170)
if (type(x) == int) & (type(y) == int):
    st.success('お釣り計算を開始します．')

    st.text(f"所持金{x}円で, {y}円の商品を買った時のおつりは...\n")
    if x < y:
        st.text("お金がたりません")
    else:

        y_10k = y // 10000
        y_tmp = y % 10000
        x_tmp = x - y_10k * 10000

        species = np.array([10000, 5000, 1000, 500, 100, 50, 10, 5, 1])

        n10000 = x_tmp // 10000
        n5000 = x_tmp % 10000 // 5000
        n1000 = x_tmp % 5000 // 1000
        n500 = x_tmp % 1000 // 500
        n100 = x_tmp % 500 // 100
        n50 = x_tmp % 100 // 50
        n10 = x_tmp % 50 // 10
        n5 = x_tmp % 10 // 5
        n1 = x_tmp % 5

        coins=np.array([n10000, n5000, n1000, n500, n100, n50, n10, n5, n1,])

        for a,b,c,d,e,f,g,h,i in itertools.product(list(range(coins[0]+1)), 
                                             list(range(coins[1]+1)),
                                             list(range(coins[2]+1)), 
                                             list(range(coins[3]+1)),
                                             list(range(coins[4]+1)), 
                                             list(range(coins[5]+1)),
                                             list(range(coins[6]+1)), 
                                             list(range(coins[7]+1)),
                                             list(range(coins[8]+1)),
                                            ):
            total = sum(np.array([a,b,c,d,e,f,g,h,i]) * species)
            if y_tmp<=total:
                ans = total - y_tmp
                #print(ans)
                break

        # amariを超える最小の硬貨
        st.text(f"{ans}円です．")
else:
    st.warning("数字を入力して下さい")
