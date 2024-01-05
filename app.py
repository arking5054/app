import streamlit as st

level = ["Daily", "Monthly", "Annually"]

def compound_interest(principal, rate, time, n):
    future_value = principal * (1 + rate/n)**(n*time)
    return future_value

def main():
    st.title("Compound Interest Calculator")

    principal = st.number_input("Enter the principal amount:", min_value=0.0, value=1000.0)
    interest_rate_type = st.radio("Select interest rate type:", level, index=0)
    interest_rate = st.number_input(f"Enter the {interest_rate_type.lower()} interest rate (%):", min_value=0.0, value=5.0, step=0.1)
    compounding_period = st.radio("Select compounding period:", level, index=2)
    time = st.number_input("Enter the number of years:", min_value=0, value=1)

    if interest_rate_type == level[0]:
        rate = interest_rate / 36500
    elif interest_rate_type == level[1]:
        rate = interest_rate / 1200
    else:
        rate = interest_rate / 100

    if compounding_period == level[0]:
        n = 365
    elif compounding_period == level[1]:
        n = 12

    if st.button("Calculate Future Value"):
        future_value = compound_interest(principal, rate, time, 1 if compounding_period == "Annually" else n)

        st.subheader("Results:")
        st.success(f"The future value of the investment is: ${future_value:.2f}")

if __name__ == "__main__":
    main()

