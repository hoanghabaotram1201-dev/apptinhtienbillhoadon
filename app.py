orient="index"
            )

            st.table(df)

            tam_tinh = df["Thành tiền"].sum()

            giam = tam_tinh * 0.05 if tam_tinh > 1000000 else 0

            tong = tam_tinh - giam

            st.write(f"### Tạm tính: {tam_tinh:,.0f} VNĐ")

            st.write(f"### Giảm giá: {giam:,.0f} VNĐ")

            st.success(f"### Tổng thanh toán: {tong:,.0f} VNĐ")

            colA, colB = st.columns(2)

            with colA:

                if st.button("💰 Thanh toán"):

                    st.session_state.bills.append({

                        "Bàn": table_number,

                        "Thời gian": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),

                        "Chi tiết": df.to_dict("records"),

                        "Tổng tiền": tong
                    })

                    st.success("Đã thanh toán.")

                    st.session_state.order_dict = {}

                    st.rerun()

            with colB:

                if st.button("🗑️ Xóa giỏ"):

                    st.session_state.order_dict = {}

                    st.rerun()

        else:

            st.info("Chưa có món.")

# ==========================================================
# TRANG ADMIN
# ==========================================================
else:

    st.header("📋 Quản lý hóa đơn")

    if len(st.session_state.bills) == 0:

        st.info("Chưa có hóa đơn.")

    else:

        bill_df = pd.DataFrame([
            {
                "Bàn": b["Bàn"],
                "Thời gian": b["Thời gian"],
                "Tổng tiền": b["Tổng tiền"]
            }
            for b in st.session_state.bills
        ])

        st.dataframe(
            bill_df,
            use_container_width=True
        )

        st.metric(
            "Tổng doanh thu",
            f"{bill_df['Tổng tiền'].sum():,.0f} VNĐ"
        )

        st.divider()

        st.subheader("Chi tiết hóa đơn")

        for i, bill in enumerate(st.session_state.bills):

            with st.expander(
                f"Bàn {bill['Bàn']} - {bill['Thời gian']}"
            ):

                detail = pd.DataFrame(bill["Chi tiết"])

                st.table(detail)

                st.write(
                    f"### Tổng tiền: {bill['Tổng tiền']:,.0f} VNĐ"
                )
          
