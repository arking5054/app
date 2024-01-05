import streamlit as st

level = ["Daily", "Weekly", "Monthly", "Quaterly", "Annually"]
level2 = ["Daily", "Weekly", "Semi-Monthly", "Monthly", "Quaterly", "Half-Yearly", "Annually"]

def compound_interest(principal, rate, time, n):
    future_value = principal * (1 + rate/n)**(n*time)
    return future_value

def main():
    st.title("Compound Interest Calculator")

    principal = st.number_input("Enter the principal amount:", min_value=0.0, value=1000.0)
    interest_rate_type = st.radio("Select interest rate type:", level, index=0)
    interest_rate = st.number_input(f"Enter the {interest_rate_type.lower()} interest rate (%):", min_value=0.0, value=5.0, step=0.1)
    compounding_period = st.radio("Select compounding period:", level2, index=2)
    time = st.number_input("Enter the number of years:", min_value=0, value=1)

    if interest_rate_type == level[0]:
        rate = interest_rate / 36500
    elif interest_rate_type == level[1]:
        a = (365/7) * 100
        rate = interest_rate / a
    elif interest_rate_type == level[2]:
        rate = interest_rate / 1200
    elif interest_rate_type == level[3]:
        rate = interest_rate / 400
    else:
        rate = interest_rate / 100

    if compounding_period == level2[0]:
        n = 365
    elif compounding_period == level2[1]:
        n = 365/7
    elif compounding_period == level2[2]:
        n = 24
    elif compounding_period == level2[3]:
        n = 12
    elif compounding_period == level2[4]:
        n = 4
    elif compounding_period == level2[5]:
        n = 2

    if st.button("Calculate Future Value"):
        future_value = compound_interest(principal, rate, time, 1 if compounding_period == level2[6] else n)

        st.subheader("Results:")
        st.success(f"The future value of the investment is: ${future_value:.2f}")

if __name__ == "__main__":
    main()
