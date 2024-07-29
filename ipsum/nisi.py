import time

# Check if BW_SESSION is valid
if BW_SESSION is None or time.time() - BW_SESSION['created_time'] > SESSION_EXPIRY_TIME:
    # Set up a new BW_SESSION
    BW_SESSION = {
        'session_id': generate_session_id(),
        'created_time': time.time()
    }
