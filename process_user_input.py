import pandas as pd
import plotly.graph_objects as go
import spacy
import re
import numpy as np

# Load the spaCy model
nlp = spacy.load("en_core_web_lg")

# Predefined list of plot types we expect
plot_types = ["scatter", "bar", "line", "pie", "histogram", "box", "area", "bubble", "dot", "heatmap"]


# Function to plot the required graphs
def graph_plotting(plot_info):

    # Create the plot
    fig = go.Figure()

    # Read user submitted file
    df = pd.read_csv('User Files/input_df.csv')

    # Create column name variables based on how many columns user has supplied
    if len(plot_info['columns']) == 1:
        # Get column names
        column_x_name = plot_info['columns'][0][6:].strip()

    elif len(plot_info['columns']) == 2:
        # Get column names
        column_x_name = plot_info['columns'][0][6:].strip()
        column_y_name = plot_info['columns'][1][6:].strip()

    elif len(plot_info['columns']) == 3:
        # Get column names
        column_x_name = plot_info['columns'][0][6:].strip()
        column_y_name = plot_info['columns'][1][6:].strip()
        column_z_name = plot_info['columns'][2][6:].strip()

    elif len(plot_info['columns']) == 4:
        # Get column names
        column_x_name = plot_info['columns'][0][6:].strip()
        column_y_name = plot_info['columns'][1][6:].strip()
        column_z_name = plot_info['columns'][2][6:].strip()
        column_z1_name = plot_info['columns'][2][6:].strip()


    # Plot scatterplot
    if ((plot_info['plot_type'] == 'scatter') and (column_x_name in df.columns) and (column_y_name in df.columns)
            and (len(plot_info['columns']) == 2)):

        # Plot scatter plot
        fig.add_trace(go.Scatter(
            x=df[column_x_name],
            y=df[column_y_name],
            mode='markers',
            name='Data Points',
            marker=dict(color='blue', size=10)
        ))

        # Add titles and labels
        fig.update_layout(
            title='Scatter Plot between ' + column_x_name + ' and ' + column_y_name,  # Title of the plot
            xaxis_title= str(column_x_name),  # X-axis label
            yaxis_title= str(column_y_name),  # Y-axis label
            template='plotly',  # Optional: Add a plotly template for a styled layout
            showlegend=True  # Show the legend
        )

        # Show the plot
        fig.show()


    # Plot bar plot
    if ((plot_info['plot_type'] == 'bar') and (column_x_name in df.columns) and (column_y_name in df.columns) and
            (len(plot_info['columns']) == 2)):

        # Get average per the category
        category_avg = df.groupby(column_x_name)[column_y_name].mean().reset_index()

        # Plot bar plot
        fig.add_trace(go.Bar(
            x=category_avg[column_x_name],  # Categories for the x-axis
            y=category_avg[column_y_name],  # Values for the y-axis
            name='Bar values',  # Legend name for the bar plot
            marker=dict(color='royalblue')  # Customize bar color (optional)
        ))

        # Add titles and labels
        fig.update_layout(
            title='Bar Plot showing average values between Category column ' + column_x_name + ' and Value Column '
                  + column_y_name,  # Title of the plot
            xaxis_title= str(column_x_name),  # X-axis label
            yaxis_title= str(column_y_name),  # Y-axis label
            template='plotly',  # Optional: Add a plotly template for a styled layout
            showlegend=True  # Show the legend
        )

        # Show the plot
        fig.show()



    # Plot line plot
    if ((plot_info['plot_type'] == 'line') and (column_x_name in df.columns) and (column_y_name in df.columns)
            and (len(plot_info['columns']) == 2)):

        # Plot line plot
        fig.add_trace(go.Scatter(
            x=df[column_x_name],
            y=df[column_y_name],
            mode='lines+markers',
            name='Line',
            marker=dict(color='blue', size=10)
        ))

        # Add titles and labels
        fig.update_layout(
            title='Line Plot between ' + column_x_name + ' and ' + column_y_name,  # Title of the plot
            xaxis_title= str(column_x_name),  # X-axis label
            yaxis_title= str(column_y_name),  # Y-axis label
            template='plotly',  # Optional: Add a plotly template for a styled layout
            showlegend=True  # Show the legend
        )

        # Show the plot
        fig.show()


    # Plot piechart
    if ((plot_info['plot_type'] == 'pie') and (column_x_name in df.columns) and (column_y_name in df.columns)
            and (len(plot_info['columns']) == 2)):

        # Plot piechart
        fig = go.Figure(data=[go.Pie(labels=df[column_x_name], values=df[column_y_name], hole=0.3)])

        # Update the layout to center the title
        fig.update_layout(
            title={
                'text': 'Pie Chart Plot between ' + column_x_name + ' and ' + column_y_name,  # Title text
                'x': 0.5,  # Center the title horizontally
                'xanchor': 'center',  # Align title to the center horizontally
                'y': 0.95,  # Position title closer to the top (adjust as needed)
                'yanchor': 'top'  # Align title to the top of the plot
            },
            annotations=[  # Label in the center of the pie chart
                dict(
                    text=str(column_x_name),  # Text in the center
                    x=0.5,  # Horizontal position
                    y=0.5,  # Vertical position
                    font_size=20,
                    showarrow=False
                )
            ],
            margin=dict(t=50, b=50, l=50, r=50)  # Adjusting margins
        )

        # Show the plot
        fig.show()

    # Plot histogram
    if (plot_info['plot_type'] == 'histogram') and (column_x_name in df.columns) and (len(plot_info['columns']) == 1):

        # Calculate start, end, and bin size
        start = df[column_x_name].min()
        end = df[column_x_name].max()

        # Adjust end to ensure it is a multiple of the bin size (optional)
        end = np.ceil(end / 10) * 10  # Round up to the nearest multiple of 10

        # Create histogram
        fig = go.Figure(data=[go.Histogram(x=df[column_x_name], xbins=dict(start=start, end=end, size=10),
                                           texttemplate='%{y}',  # Display frequency (y-value) above the bar
                                           textposition='outside',  # Position the text outside the bars
                                            )])

        # Update layout for titles and axis labels
        fig.update_layout(
            title='Histogram of Column ' + column_x_name,  # Plot title
            xaxis_title="Column " + column_x_name,  # X-axis label
            yaxis_title='Frequency of Occurence',  # Y-axis label
            bargap=0.2  # Set the gap between bars (values between 0 and 1)
        )

        # Show the plot
        fig.show()


    # Plot boxplot
    if (plot_info['plot_type'] == 'box') and (column_x_name in df.columns) and (column_y_name in df.columns) and (
            len(plot_info['columns']) == 2):

        # Create a box plot
        fig = go.Figure(data=[go.Box(
            x=df[column_x_name],  # Categorical variable (e.g., Male/Female)
            y=df[column_y_name],  # Numerical variable (e.g., Salary)
            boxmean='sd',  # Display the mean and standard deviation
        )])

        # Update layout with titles
        fig.update_layout(
            title='Pie Chart Plot between ' + column_x_name + ' and ' + column_y_name,
            xaxis_title=column_x_name,
            yaxis_title=column_y_name,
        )

        fig.show()

    # Plot areachart
    if ((plot_info['plot_type'] == 'area') and (column_x_name in df.columns) and (column_y_name in df.columns) and
            (column_z_name in df.columns) and (column_z1_name in df.columns) and (len(plot_info['columns']) == 4)):

        # Trace for the first category
        fig.add_trace(go.Scatter(
            x=df[column_x_name],
            y=df[column_y_name],
            fill='tonexty',  # Fills the area between the line and the previous one
            mode='none',  # Hides the line, only fills the area
            name=column_y_name,
            stackgroup='one'  # Group this trace as part of the stacked areas
        ))

        # Trace for the second category
        fig.add_trace(go.Scatter(
            x=df[column_x_name],
            y=df[column_z_name],
            fill='tonexty',
            mode='none',
            name=column_z_name,
            stackgroup='one'  # Stacked with the first trace
        ))

        # Trace for the third category
        fig.add_trace(go.Scatter(
            x=df[column_x_name],
            y=df[column_z1_name],
            fill='tonexty',
            mode='none',
            name=column_z1_name,
            stackgroup='one'  # Stacked with the other two traces
        ))

        # Add titles and labels
        fig.update_layout(
            title='Stacked Area Chart with Category ' + column_x_name,
            xaxis_title=column_x_name,
            yaxis_title='values',
            template='plotly_dark'  # Optional: Set a dark template
        )

        # Show the chart
        fig.show()

    # Plot bubble chart
    if ((plot_info['plot_type'] == 'bubble') and (column_x_name in df.columns) and (column_y_name in df.columns) and
            (column_z_name in df.columns) and (column_z1_name in df.columns) and (len(plot_info['columns']) == 4)):

        # Create the bubble chart
        fig = go.Figure(go.Scatter(
            x=df[column_x_name],
            y=df[column_y_name],
            mode='markers',  # Indicates we are creating a scatter plot (with markers)
            marker=dict(
                size=df[column_z_name],  # Bubble size
                color=df[column_z1_name],  # Bubble color
                colorscale='Viridis',  # Color scale for the bubbles
                showscale=True,  # Show color scale on the side
                opacity=0.6  # Transparency of the bubbles
            ),
            text=column_x_name,  # Hover text showing country names
            hovertemplate=
            f'<b>%{column_x_name}</b><br>' +  # Display country name in bold
            'GDP: %{x} Trillion USD<br>' +  # Show GDP value (x-axis)
            'Life Expectancy: %{y} Years<br>' +  # Show life expectancy (y-axis)
            'Population: %{customdata} Million<br>' +  # Show population (custom data)
            '<extra></extra>'  # Hide the extra box
        ))

        # Add titles and labels
        fig.update_layout(
            title='Bubble Chart',
            xaxis_title=column_x_name,
            yaxis_title='Y Value',
            template='plotly_dark'  # Optional: dark template for aesthetics
        )

        # Show the chart
        fig.show()

    # Plot dotplot
    if ((plot_info['plot_type'] == 'dot') and (column_x_name in df.columns) and (column_y_name in df.columns)
            and (len(plot_info['columns']) == 2)):

        # Create a dot plot
        fig = go.Figure(go.Scatter(
            x=df[column_x_name],
            y=df[column_y_name],
            mode='markers',  # Display as individual points (dots)
            marker=dict(
                size=12,  # Size of each dot
                color='blue',  # Color of the dots
                opacity=0.6  # Transparency of the dots
            )
        ))

        # Add titles and labels
        fig.update_layout(
            title='Dot Plot between ' + column_x_name + ' and ' + column_y_name,
            xaxis_title=column_x_name,
            yaxis_title=column_y_name,
            template='plotly_dark'  # Optional: dark template for aesthetics
        )

        # Show the chart
        fig.show()

    # Plot heatmap
    if ((plot_info['plot_type'] == 'heatmap') and (column_x_name in df.columns) and (column_y_name in df.columns) and
            (column_z_name in df.columns) and (column_z1_name in df.columns) and (len(plot_info['columns']) == 4)):

        # Filter dataset with the requested columns
        dataset = df[[column_x_name, column_y_name, column_z_name, column_z1_name]]

        # Create heatmap
        fig = go.Figure(data=go.Heatmap(
            z=dataset.values,  # 2D matrix (values from DataFrame)
            x=dataset.columns,  # Column names will be on the x-axis
            y=dataset.index,  # Index values will be on the y-axis
            colorscale='Viridis',  # Choose a colorscale (can be customized)
            colorbar=dict(title="Value"),  # Title for the color bar
        ))

        # Add titles and labels
        fig.update_layout(
            title='Heatmap between various X-axis columns and ' + column_z1_name,
            xaxis_title='Various columns',
            yaxis_title=column_z1_name,
            template='plotly_dark'  # Optional: dark template for aesthetics
        )

        # Show the plot
        fig.show()




    else:
        print("Please check your supplied graphical plot name and also make sure the columns supplied are present "
              "in the uploaded data file ")

    # Return figure
    return fig



# Function to understand required plot type and column names
def process_user_input(input_text):

    # Process the text with spaCy NLP pipeline
    doc = nlp(input_text)

    # Initialize the plot type and columns to None
    plot_type = None
    columns = []

    # Identify plot type based on keywords in the text
    for plot in plot_types:
        if plot in input_text.lower():
            plot_type = plot
            break  # Stop once the plot type is identified

    if not plot_type:
        return {"error": "Plot type not recognized. Please specify a valid plot type."}

    # Extract column names by looking for capitalized words (assuming column names are capitalized)
    # Example: Column A, Column B, etc.
    column_pattern = r"Column\s+[A-Za-z0-9]+"  # Regex to match "Column X"
    columns = re.findall(column_pattern, input_text)

    # If no columns found, return an error
    if not columns:
        return {"error": "No columns found. Please specify the columns for the plot."}

    # Return the recognized plot type and columns
    return {"plot_type": plot_type, "columns": columns}

# # Get information involved in user instruction for creation of plots
# plot_info = process_user_input("Please create a heatmap for Column Age, Column Id, Column 0 and Column Unnamed: 0")
#
# # Plot the required graphs
# figure = graph_plotting(plot_info)

