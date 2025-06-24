import streamlit as st
import time

def calculate_learning_style(answers):
    visual_score = 0
    auditory_score = 0
    kinesthetic_score = 0

    # Pertanyaan 1: Cara belajar yang paling efektif
    if answers[0] == "Melihat diagram, grafik, atau video":
        visual_score += 1
    elif answers[0] == "Mendengarkan ceramah atau diskusi":
        auditory_score += 1
    elif answers[0] == "Melakukan praktik langsung atau eksperimen":
        kinesthetic_score += 1

    # Pertanyaan 2: Saat mencoba memahami instruksi baru
    if answers[1] == "Saya perlu melihat demonstrasi":
        visual_score += 1
    elif answers[1] == "Saya perlu mendengarkan penjelasan lisan":
        auditory_score += 1
    elif answers[1] == "Saya perlu mencoba melakukannya sendiri":
        kinesthetic_score += 1

    # Pertanyaan 3: Saat mengingat informasi
    if answers[2] == "Saya mengingat apa yang saya lihat":
        visual_score += 1
    elif answers[2] == "Saya mengingat apa yang saya dengar":
        auditory_score += 1
    elif answers[2] == "Saya mengingat apa yang saya lakukan":
        kinesthetic_score += 1

    # Pertanyaan 4: Saat membaca buku
    if answers[3] == "Saya lebih suka membaca dengan gambar atau ilustrasi":
        visual_score += 1
    elif answers[3] == "Saya lebih suka membaca sambil mendengarkan atau berbicara sendiri":
        auditory_score += 1
    elif answers[3] == "Saya suka menggarisbawahi atau membuat catatan fisik":
        kinesthetic_score += 1

    # Pertanyaan 5: Dalam lingkungan belajar
    if answers[4] == "Saya lebih suka tempat yang rapi dan terorganisir":
        visual_score += 1
    elif answers[4] == "Saya tidak keberatan dengan sedikit kebisingan latar belakang":
        auditory_score += 1
    elif answers[4] == "Saya perlu bergerak atau mengubah posisi sesekali":
        kinesthetic_score += 1

    scores = {
        "Visual": visual_score,
        "Auditori": auditory_score,
        "Kinestetik": kinesthetic_score
    }

    max_score = max(scores.values())
    dominant_styles = [style for style, score in scores.items() if score == max_score]

    return dominant_styles, scores

def run_app():
    st.set_page_config(page_title="Kalkulator Gaya Belajar", page_icon="🧠")

    st.title("🧠 Kalkulator Gaya Belajar")
    st.write("Jawablah pertanyaan-pertanyaan berikut untuk mengetahui gaya belajar dominan Anda.")
    st.markdown("---")

    questions = [
        "1. Cara belajar yang paling efektif bagi saya adalah:",
        "2. Saat mencoba memahami instruksi baru, saya cenderung:",
        "3. Saat mengingat informasi, saya cenderung:",
        "4. Saat membaca buku, saya lebih suka:",
        "5. Dalam lingkungan belajar, saya cenderung:",
    ]

    options = [
        ["Melihat diagram, grafik, atau video", "Mendengarkan ceramah atau diskusi", "Melakukan praktik langsung atau eksperimen"],
        ["Saya perlu melihat demonstrasi", "Saya perlu mendengarkan penjelasan lisan", "Saya perlu mencoba melakukannya sendiri"],
        ["Saya mengingat apa yang saya lihat", "Saya mengingat apa yang saya dengar", "Saya mengingat apa yang saya lakukan"],
        ["Saya lebih suka membaca dengan gambar atau ilustrasi", "Saya lebih suka membaca sambil mendengarkan atau berbicara sendiri", "Saya suka menggarisbawahi atau membuat catatan fisik"],
        ["Saya lebih suka tempat yang rapi dan terorganisir", "Saya tidak keberatan dengan sedikit kebisingan latar belakang", "Saya perlu bergerak atau mengubah posisi sesekali"],
    ]

    user_answers = []
    for i, question in enumerate(questions):
        st.subheader(question)
        answer = st.radio(f"Pilih salah satu untuk pertanyaan {i+1}", options[i], key=f"q{i}")
        user_answers.append(answer)
        st.markdown("---")

    if st.button("Hitung Gaya Belajar"):
        st.info("Menghitung gaya belajar Anda...")

        # Animasi sederhana
        progress_bar = st.progress(0)
        status_text = st.empty()
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
            status_text.text(f"Progress: {percent_complete + 1}%")
        time.sleep(0.5)
        progress_bar.empty()
        status_text.empty()

        dominant_styles, scores = calculate_learning_style(user_answers)

        st.success("Perhitungan Selesai!")
        st.subheader("🎉 Gaya Belajar Dominan Anda adalah:")

        if len(dominant_styles) == 1:
            st.markdown(f"## **{dominant_styles[0]}**")
            if dominant_styles[0] == "Visual":
                st.image("https://media.giphy.com/media/l4KkiJzD2VwY/giphy.gif", caption="Gaya Belajar Visual", width=200)
                st.write("Anda belajar paling baik melalui melihat, seperti diagram, grafik, video, atau membaca.")
            elif dominant_styles[0] == "Auditori":
                st.image("https://media.giphy.com/media/3o7qDD03H9h1K/giphy.gif", caption="Gaya Belajar Auditori", width=200)
                st.write("Anda belajar paling baik melalui mendengarkan, seperti ceramah, diskusi, atau audio.")
            elif dominant_styles[0] == "Kinestetik":
                st.image("https://media.giphy.com/media/l4Kk0Z2V1XvQ/giphy.gif", caption="Gaya Belajar Kinestetik", width=200)
                st.write("Anda belajar paling baik melalui melakukan, seperti praktik langsung, eksperimen, atau gerakan.")
        else:
            st.write("Anda memiliki kombinasi gaya belajar:")
            for style in dominant_styles:
                st.markdown(f"### **{style}**")
            st.write("Anda mungkin menggabungkan beberapa cara belajar untuk hasil terbaik.")

        st.subheader("Rincian Skor:")
        st.write(f"- Visual: {scores['Visual']} poin")
        st.write(f"- Auditori: {scores['Auditori']} poin")
        st.write(f"- Kinestetik: {scores['Kinestetik']} poin")

        st.markdown("---")
        st.write("Ingatlah, ini hanyalah panduan. Anda mungkin menggunakan kombinasi gaya belajar yang berbeda dalam situasi yang berbeda.")

if __name__ == "__main__":
    run_app()
