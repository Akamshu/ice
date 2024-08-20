import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def solve_linear_equation(a, b):
    """
    Solves the linear equation ax + b = 0
    Returns the value of x.
    """
    if a == 0:
        raise ValueError("The coefficient 'a' cannot be 0 in a linear equation.")
    return -b / a

def plot_linear_equation(a, b):
    """
    Plots the graph of the linear equation y = ax + b
    """
    # Generate x values
    x_values = np.linspace(-10, 10, 400)
    
    # Compute y values
    y_values = a * x_values + b
    
    # Plot the graph
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=f'y = {a}x + {b}', color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    # Mark the solution on the graph
    x_solution = solve_linear_equation(a, b)
    plt.scatter(x_solution, 0, color='red', label=f'Solution: x = {x_solution}')
    
    # Adding labels and title
    plt.title('Graph of Linear Equation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    
    # Streamlit plot
    st.pyplot(plt)

# Streamlit user interface
st.sidebar.title("Linear Equation Solver")
page = st.sidebar.selectbox("Select a page", ["About", "Linear Equation Solver"])

if page == "Linear Equation Solver":
    st.title("Linear Equation Solver and Plotter")

    # Inputs for 'a' and 'b'
    a = st.number_input("Enter the value of 'a' (coefficient of x):", value=1.0, step=0.1)
    b = st.number_input("Enter the value of 'b' (constant term):", value=0.0, step=0.1)

    # Solve the equation
    if st.button("Solve"):
        try:
            solution = solve_linear_equation(a, b)
            st.write(f"The solution to the equation {a}x + {b} = 0 is x = {solution}")
            
            # Plot the graph
            plot_linear_equation(a, b)

        except ValueError as e:
            st.error(e)

elif page == "About":
    st.title("About This App")
    image_path = "home_page.jpg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
    Welcome to the Streamlit app for solving and plotting linear equations of the form `ax + b = 0`.
    
    - **Linear Equation Solver:** Allows you to input the coefficients `a` and `b` and calculates the solution for `x`.
    - **Graph Plotting:** Displays a graph of the linear equation with the calculated solution highlighted on the graph.
    
    **Developed using:**
    - Python
    - Streamlit
    - Matplotlib
    """)

