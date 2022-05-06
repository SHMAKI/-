import streamlit as st

st.title('理系でも出来るお釣り計算_改良版')
st.text("前提条件: 硬貨と紙幣の枚数は最小と仮定します")
st.text("手持ちの硬貨と紙幣の数をなるべく減らすように計算します")
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

        y_tmp_keta = len(str(y_tmp))
        # 各位を比較し、４パタンで場合分け
        total_list = [0,0,0,0,0]
        #kuriagari = 0
        for z in range(y_tmp_keta):
            y_keta = int(str(y_tmp)[-(1+z)])
            x_keta = int(str(x_tmp)[-(1+z)])
            if y_keta <= x_keta:
                if y_keta % 5  <= x_keta % 5:
                    total_list[-(1+z)] = y_keta
                else:
                    total_list[-(1+z)] = 5
            elif y_keta % 5 <= x_keta % 5:
                total_list[-(1+z)] = y_keta % 5
        #    else:
        #total_list[-(2+z)] = kuriagari
        total = int("".join( map(str, total_list)))

        ans = total - y_tmp
        pay = total + y_10k * 10000
        st.text(f"{pay}円の支払い，{ans}円のお釣りになります．")
else:
    st.warning("数字を入力して下さい")
