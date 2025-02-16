import streamlit as st
from streamlit_quill import st_quill
import openai
from fpdf import FPDF
from io import BytesIO

from openai import AzureOpenAI  
from leftnavigation import render_left_navigation
from popup import edit_prompt_popup

client = AzureOpenAI(  
      api_key="",  
      api_version="2024-02-01",  
      azure_endpoint=""  
  ) 

# This will correspond to the custom name you chose for your deployment when you deployed a model.  
# Use a gpt-35-turbo-instruct deployment.  
deployment_name = "PLSTest"  

# Handle the popup for editing prompts
edit_prompt_popup()

# Call the render_left_navigation function to display the sidebar
final_prompt = render_left_navigation()


user_input = "k"

if user_input:
    with st.spinner("Processing..."):
            # Call the Azure OpenAI API
            # Send a completion call to generate an answer  
              

            # Extract and print the assistant's reply
        processed_text = """
<h1>Exploring the Wonders of the Universe</h1>

<p>The universe is a vast expanse, filled with mysteries and phenomena that have fascinated humanity for centuries. From the smallest subatomic particles to the largest galaxies, the cosmos offers endless opportunities for exploration and discovery.</p>

<h2>The Beauty of Nebulas</h2>

<p>Nebulas are vast clouds of gas and dust in space, often serving as the birthplace of stars. Their mesmerizing colors and shapes have been captured in stunning images by telescopes.</p>

<img src="https://picsum.photos/200/300" alt="Image of a Nebula">

<p>Some famous nebulas include:</p>

<ul>
  <li>The <strong>Orion Nebula</strong></li>
  <li>The <em>Helix Nebula</em></li>
  <li>The <u>Crab Nebula</u></li>
</ul>

<h2>Black Holes: The Cosmic Enigmas</h2>

<p>Black holes are regions in space where the gravitational pull is so strong that nothing, not even light, can escape. They challenge our understanding of physics and continue to be a major focus of astronomical research.</p>

<blockquote>
  "Black holes are where God divided by zero." – <strong>Albert Einstein</strong>
</blockquote>

<h3>Understanding Event Horizons</h3>

<p>The event horizon of a black hole is the boundary beyond which nothing can return. It's a point of no return, making black holes even more intriguing.</p>

<h2>The Quest for Exoplanets</h2>

<p>Exoplanets are planets that orbit stars outside our solar system. The search for Earth-like exoplanets has intensified, with the hope of finding signs of life elsewhere in the universe.</p>

<ol>
  <li>Detection Methods:
    <ul>
      <li>Transit Method</li>
      <li>Radial Velocity Method</li>
    </ul>
  </li>
  <li>Notable Discoveries:
    <ul>
      <li>Kepler-186f</li>
      <li>Proxima Centauri b</li>
    </ul>
  </li>
</ol>

<h2>The Role of Dark Matter and Dark Energy</h2>

<p>While dark matter and dark energy cannot be observed directly, their effects on the universe are profound. They are believed to make up most of the universe's mass-energy content.</p>

<pre>
<code>
// Sample code to calculate gravitational force
def gravitational_force(m1, m2, r):
    G = 6.67430e-11  # gravitational constant
    return G * (m1 * m2) / r**2
</code>
</pre>

<p>For more information on the universe and its wonders, visit <a href="https://www.nasa.gov">NASA's official website</a>.</p>

"""
           
            # Update session state with the processed text
        st.session_state.processed_text = processed_text
else:
        st.warning("Please enter some text to process.")

# Display the Quill editor with the processed text
if 'processed_text' in st.session_state:
    st_quill(value=st.session_state.processed_text, key="quill_editor")    


    