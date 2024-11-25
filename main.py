import streamlit as st
from database.connection import init_database
from components.search import render_search
from components.statistics import render_statistics
from components.submission_form import render_submission_form
from components.viewer import render_references

def main():
    st.set_page_config(
        page_title="Zambian Wikipedia Reference Portal",
        page_icon="📚",
        layout="wide"
    )
    
    st.title("Zambian Wikipedia Reference Portal")
    
    # Initialize database
    init_database()
    
    # Render statistics
    render_statistics()
    
    # Render search
    category, search_term = render_search()
    
    # Display references based on search/filter
    render_references(category, search_term)
    
    # Show submission form
    with st.sidebar:
        render_submission_form()

if __name__ == "__main__":
    main()
