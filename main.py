import streamlit as st
import datetime
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Page configuration
st.set_page_config(
    page_title="TNPSC Group 4 Countdown",
    page_icon="⏰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for stunning visuals
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .exam-info {
        text-align: center;
        font-size: 1.5rem;
        color: #4a5568;
        margin-bottom: 3rem;
        padding: 1rem;
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .countdown-container {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 3rem 0;
        flex-wrap: wrap;
    }
    
    .time-unit {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        min-width: 150px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        transform: perspective(1000px) rotateX(5deg);
        transition: all 0.3s ease;
    }
    
    .time-unit:hover {
        transform: perspective(1000px) rotateX(0deg) translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }
    
    .time-number {
        font-size: 3rem;
        font-weight: bold;
        display: block;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .time-label {
        font-size: 1.2rem;
        margin-top: 0.5rem;
        opacity: 0.9;
    }
    
    .motivational-text {
        text-align: center;
        font-size: 1.3rem;
        color: #2d3748;
        margin: 3rem 0;
        padding: 2rem;
        background: linear-gradient(135deg, #ffeef8, #f0fff4);
        border-radius: 15px;
        border-left: 5px solid #38a169;
    }
    
    .progress-container {
        margin: 2rem 0;
    }
    
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 50%, #4facfe 100%);
        min-height: 100vh;
    }
</style>
""", unsafe_allow_html=True)

def calculate_countdown():
    """Calculate time remaining until exam date"""
    now = datetime.datetime.now()
    exam_date = datetime.datetime(2025, 7, 12, 9, 0, 0)  # Assuming 9 AM exam time
    
    if now > exam_date:
        return None, "Exam day has passed!"
    
    time_remaining = exam_date - now
    
    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'total_seconds': time_remaining.total_seconds()
    }, None

def create_progress_chart(time_data):
    """Create a beautiful progress visualization"""
    total_days = 40  # Total days from June 2 to July 12
    remaining_days = time_data['days']
    completed_days = total_days - remaining_days
    
    # Create a circular progress chart
    fig = go.Figure(data=[
        go.Pie(
            values=[completed_days, remaining_days],
            labels=['Days Completed', 'Days Remaining'],
            hole=0.7,
            marker_colors=['#38a169', '#e53e3e'],
            textinfo='none',
            hovertemplate='%{label}: %{value} days<extra></extra>'
        )
    ])
    
    fig.update_layout(
        title={
            'text': f"Progress: {completed_days}/{total_days} Days",
            'x': 0.5,
            'font': {'size': 20, 'color': 'white'}
        },
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': 'white'},
        height=300
    )
    
    # Add center text
    fig.add_annotation(
        text=f"{(completed_days/total_days)*100:.1f}%<br>Complete",
        x=0.5, y=0.5,
        font_size=20,
        font_color="white",
        showarrow=False
    )
    
    return fig

def get_motivational_message(days_remaining):
    """Get motivational message based on days remaining"""
    if days_remaining > 30:
        return "🎯 You have plenty of time! Create a solid study plan and stick to it."
    elif days_remaining > 20:
        return "📚 Great! You're in the perfect preparation zone. Focus on your weak areas."
    elif days_remaining > 10:
        return "⚡ Time to intensify! Practice more mock tests and revise thoroughly."
    elif days_remaining > 5:
        return "🔥 Final sprint mode! Review important topics and stay confident."
    else:
        return "💪 You're almost there! Stay calm, revise key points, and believe in yourself!"

# Main app
def main():
    # Header
    st.markdown('<h1 class="main-header">🎓 TNPSC Group 4 Exam Countdown</h1>', unsafe_allow_html=True)
    
    # Exam info
    st.markdown('''
    <div class="exam-info">
        📅 <strong>Exam Date:</strong> July 12, 2025<br>
        🏛️ <strong>Tamil Nadu Public Service Commission</strong><br>
        📍 <strong>Group 4 (Combined Civil Services Examination)</strong>
    </div>
    ''', unsafe_allow_html=True)
    
    # Create a placeholder for auto-refresh
    countdown_placeholder = st.empty()
    progress_placeholder = st.empty()
    motivation_placeholder = st.empty()
    
    # Auto-refresh every second
    while True:
        time_data, error_msg = calculate_countdown()
        
        if error_msg:
            countdown_placeholder.error(error_msg)
            break
        
        with countdown_placeholder.container():
            # Countdown display
            st.markdown(f'''
            <div class="countdown-container">
                <div class="time-unit">
                    <span class="time-number">{time_data['days']:02d}</span>
                    <div class="time-label">DAYS</div>
                </div>
                <div class="time-unit">
                    <span class="time-number">{time_data['hours']:02d}</span>
                    <div class="time-label">HOURS</div>
                </div>
                <div class="time-unit">
                    <span class="time-number">{time_data['minutes']:02d}</span>
                    <div class="time-label">MINUTES</div>
                </div>
                <div class="time-unit">
                    <span class="time-number">{time_data['seconds']:02d}</span>
                    <div class="time-label">SECONDS</div>
                </div>
            </div>
            ''', unsafe_allow_html=True)
        
        with progress_placeholder.container():
            col1, col2 = st.columns([1, 1])
            
            with col1:
                # Progress chart
                fig = create_progress_chart(time_data)
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Study statistics
                st.markdown("### 📊 Study Stats")
                total_hours = time_data['total_seconds'] / 3600
                study_hours_per_day = 6  # Assuming 6 hours study per day
                total_study_hours = time_data['days'] * study_hours_per_day
                
                st.metric("⏰ Total Hours Left", f"{total_hours:.0f}")
                st.metric("📚 Potential Study Hours", f"{total_study_hours:.0f}")
                st.metric("🎯 Study Sessions Left", f"{total_study_hours//2:.0f}")
        
        with motivation_placeholder.container():
            # Motivational message
            message = get_motivational_message(time_data['days'])
            st.markdown(f'<div class="motivational-text">{message}</div>', unsafe_allow_html=True)
            
            # Study tips
            with st.expander("💡 Quick Study Tips"):
                st.markdown("""
                - **Daily Schedule**: Maintain 6-8 hours of focused study
                - **Mock Tests**: Take at least one mock test every 3 days
                - **Revision**: Dedicate 2 hours daily for revision
                - **Current Affairs**: Read newspapers and monthly magazines
                - **Previous Papers**: Solve last 5 years' question papers
                - **Health**: Take breaks, exercise, and maintain good sleep
                """)
        
        # Wait for 1 second before next update
        time.sleep(1)

if __name__ == "__main__":
    main()
