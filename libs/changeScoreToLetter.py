def changeScoreToLetter(score):
    if score < 0:
        return {
            "letter": 'Invalid',
            "text": 'I really want to question what you do in the class'
        }
    elif score >= 0 and score < 40:
        return {
            "letter": 'E',
            "text": 'You are so damn bad at exam!'
        }
    elif score >= 40 and score < 50:
        return {
            "letter": 'D',
            "text": 'You are bad, but not too bad'
        }
    elif score >= 50 and score < 54:
        return {
            "letter": 'C-',
            "text": 'You need to study harder!'
        }
    elif score >= 55 and score < 60:
        return {
            "letter": 'C',
            "text": 'Hufft.. too close to fail huh?'
        }
    elif score >= 60 and score < 65:
        return {
            "letter": 'C+',
            "text": 'It still bad, but I can accept it'
        }
    elif score >= 65 and score < 70:
        return {
            "letter": 'B-',
            "text": 'Good, try more harder next time!'
        }
    elif score >= 70 and score < 75:
        return {
            "letter": 'B',
            "text": 'Nice, you are safe.'
        }
    elif score >= 75 and score < 80:
        return {
            "letter": 'B+',
            "text": 'Well done, you are good enough!'
        }
    elif score >= 80 and score < 85:
        return {
            "letter": 'A-',
            "text": 'Unbelieveable, you are so close to the top!'
        }
    elif score >= 85 and score <= 100:
        return {
            "letter": 'A',
            "text": 'Congratulations, you are the smartest in the class!'
        }
    elif score > 100 and score <= 1000:
        return {
            "letter": 'S',
            "text": 'You must be the one who create the exams!'
        }
    elif score > 1000:
        return {
            "letter": 'SSSSS+',
            "text": 'OH GOD!'
        }