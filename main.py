import streamlit as st
import datetime
import time
import math

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
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 900;
        margin-bottom: 2rem;
        font-family: 'Orbitron', monospace;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 10px #667eea, 0 0 20px #667eea, 0 0 30px #667eea; }
        to { text-shadow: 0 0 20px #764ba2, 0 0 30px #764ba2, 0 0 40px #764ba2; }
    }
    
    .exam-info {
        text-align: center;
        font-size: 1.5rem;
        color: #ffffff;
        margin-bottom: 3rem;
        padding: 2rem;
        background: rgba(255,255,255,0.1);
        border-radius: 20px;
        backdrop-filter: blur(15px);
        border: 2px solid rgba(255,255,255,0.2);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    
    .countdown-container {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 3rem 0;
        flex-wrap: wrap;
    }
    
    .time-unit {
        background: linear-gradient(145deg, #ff6b6b, #ee5a24, #ff9ff3);
        color: white;
        padding: 2.5rem 1.5rem;
        border-radius: 25px;
        text-align: center;
        min-width: 160px;
        box-shadow: 
            0 15px 35px rgba(0,0,0,0.4),
            inset 0 -5px 15px rgba(0,0,0,0.2);
        transform: perspective(1000px) rotateX(10deg);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .time-unit::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        transform: rotate(45deg);
        animation: shine 3s infinite;
    }
    
    @keyframes shine {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        50% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        100% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
    }
    
    .time-unit:hover {
        transform: perspective(1000px) rotateX(0deg) translateY(-15px) scale(1.05);
        box-shadow: 
            0 25px 50px rgba(0,0,0,0.5),
            inset 0 -5px 15px rgba(0,0,0,0.2);
    }
    
    .time-number {
        font-size: 3.5rem;
        font-weight: 900;
        display: block;
        font-family: 'Orbitron', monospace;
        text-shadow: 0 0 10px rgba(255,255,255,0.5);
        position: relative;
        z-index: 2;
    }
    
    .time-label {
        font-size: 1.2rem;
        margin-top: 0.8rem;
        font-weight: 700;
        letter-spacing: 2px;
        position: relative;
        z-index: 2;
    }
    
    .progress-bar-container {
        margin: 3rem 0;
        padding: 2rem;
        background: rgba(255,255,255,0.1);
        border-radius: 20px;
        backdrop-filter: blur(10px);
    }
    
    .progress-bar {
        width: 100%;
        height: 30px;
        background: rgba(255,255,255,0.2);
        border-radius: 15px;
        overflow: hidden;
        position: relative;
        margin: 1rem 0;
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #ff6b6b, #ffa726, #66bb6a);
        border-radius: 15px;
        transition: width 0.5s ease;
        position: relative;
        overflow: hidden;
    }
    
    .progress-fill::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        animation: progress-shine 2s infinite;
    }
    
    @keyframes progress-shine {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .motivational-text {
        text-align: center;
        font-size: 1.4rem;
        color: #ffffff;
        margin: 3rem 0;
        padding: 2.5rem;
        background: linear-gradient(135deg, rgba(255,107,107,0.2), rgba(108,92,231,0.2));
        border-radius: 20px;
        border: 2px solid rgba(255,255,255,0.2);
        backdrop-filter: blur(15px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .stat-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        transition: transform 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: #ffa726;
        font-family: 'Orbitron', monospace;
    }
    
    .stat-label {
        font-size: 1rem;
        color: #ffffff;
        margin-top: 0.5rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        min-height: 100vh;
    }
    
    .tips-container {
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        padding: 1.5rem;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        margin: 2rem 0;
    }
    
    .blinking {
        animation: blink 1s infinite;
    }
    
    @keyframes blink {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0; }
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

def create_progress_bar(time_data):
    """Create a beautiful progress bar"""
    total_days = 40  # Total days from June 2 to July 12
    remaining_days = time_data['days']
    completed_days = total_days - remaining_days
    progress_percentage = (completed_days / total_days) * 100
    
    return f"""
    <div class="progress-bar-container">
        <h3 style="color: white; text-align: center; margin-bottom: 1rem;">
            📈 Preparation Progress: {progress_percentage:.1f}%
        </h3>
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress_percentage}%;"></div>
        </div>
        <div style="display: flex; justify-content: space-between; color: white; font-size: 0.9rem; margin-top: 0.5rem;">
            <span>Start: June 2</span>
            <span>{completed_days}/{total_days} days</span>
            <span>Exam: July 12</span>
        </div>
    </div>
    """

def get_motivational_message(days_remaining):
    """Get motivational message based on days remaining"""
    if days_remaining > 30:
        return "🎯 Excellent! You have abundant time. Create a comprehensive study plan and build strong fundamentals!"
    elif days_remaining > 20:
        return "📚 Perfect timing! You're in the golden preparation zone. Focus on covering all topics systematically."
    elif days_remaining > 10:
        return "⚡ Acceleration time! Increase your practice sessions and solve more mock tests."
    elif days_remaining > 5:
        return "🔥 Final sprint activated! Focus on revision, important formulas, and quick recall techniques."
    else:
        return "💪 Victory is near! Stay calm, trust your preparation, and maintain confidence!"

def get_study_tips():
    """Return study tips based on time remaining"""
    return """
    **🎯 Strategic Study Plan:**
    - **Daily Target**: 6-8 hours focused study + 2 hours revision
    - **Mock Tests**: Attempt 2-3 full-length tests per week
    - **Current Affairs**: 1 hour daily newspaper + monthly magazine
    - **Previous Papers**: Solve last 10 years question papers
    - **Weak Areas**: Dedicate extra 2 hours to challenging topics
    - **Health**: 7-8 hours sleep + regular exercise + healthy diet
    
    **📊 Subject-wise Time Allocation:**
    - General Studies: 40%
    - Aptitude & Mental Ability: 25%
    - General Tamil/English: 20%
    - Current Affairs: 15%
    """

# Main app
def main():
    # Header with animation
    st.markdown('<h1 class="main-header">🎓 TNPSC GROUP 4 COUNTDOWN</h1>', unsafe_allow_html=True)
    
    # Exam info
    st.markdown('''
    <div class="exam-info">
        📅 <strong>TARGET DATE:</strong> July 12, 2025 | 🕘 9:00 AM<br>
        🏛️ <strong>Tamil Nadu Public Service Commission</strong><br>
        📍 <strong>Group 4 - Combined Civil Services Examination</strong><br>
        🎯 <strong>Your Success Journey Starts Now!</strong>
    </div>
    ''', unsafe_allow_html=True)
    
    # Create containers for real-time updates
    countdown_placeholder = st.empty()
    progress_placeholder = st.empty()
    stats_placeholder = st.empty()
    motivation_placeholder = st.empty()
    
    # Auto-refresh loop
    for _ in range(86400):  # Run for 24 hours, then restart
        time_data, error_msg = calculate_countdown()
        
        if error_msg:
            st.error(f"🎉 {error_msg}")
            st.balloons()
            break
        
        # Countdown Display
        with countdown_placeholder.container():
            blink_class = "blinking" if time_data['days'] <= 7 else ""
            st.markdown(f'''
            <div class="countdown-container">
                <div class="time-unit {blink_class}">
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
        
        # Progress Bar
        with progress_placeholder.container():
            st.markdown(create_progress_bar(time_data), unsafe_allow_html=True)
        
        # Statistics
        with stats_placeholder.container():
            total_hours = time_data['total_seconds'] / 3600
            study_hours_per_day = 6
            total_study_hours = time_data['days'] * study_hours_per_day
            mock_tests = max(time_data['days'] // 3, 1)
            
            st.markdown(f'''
            <div class="stats-container">
                <div class="stat-card">
                    <div class="stat-number">{total_hours:.0f}</div>
                    <div class="stat-label">⏰ Total Hours Left</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{total_study_hours:.0f}</div>
                    <div class="stat-label">📚 Study Hours Available</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{mock_tests}</div>
                    <div class="stat-label">🎯 Mock Tests Possible</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{time_data['days'] * 2}</div>
                    <div class="stat-label">📖 Revision Sessions</div>
                </div>
            </div>
            ''', unsafe_allow_html=True)
        
        # Motivational Section
        with motivation_placeholder.container():
            message = get_motivational_message(time_data['days'])
            st.markdown(f'<div class="motivational-text">✨ {message}</div>', unsafe_allow_html=True)
            
            # Study Tips in expandable section
            with st.expander("💡 Master Study Strategy & Tips", expanded=False):
                st.markdown(get_study_tips())
            
            # Quick actions
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("🎯 Today's Goal", use_container_width=True):
                    st.success("✅ Set your daily target and track progress!")
            with col2:
                if st.button("📊 Mock Test", use_container_width=True):
                    st.info("🚀 Time for a practice test! Test your knowledge.")
            with col3:
                if st.button("💪 Motivation", use_container_width=True):
                    st.balloons()
                    st.success("🌟 You've got this! Keep pushing forward!")
        
        # Wait for 1 second before next update
        time.sleep(1)

if __name__ == "__main__":
    main()
