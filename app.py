from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/diagnose", methods=["POST"])
def diagnose():

    data = request.json

    fever = data.get("fever", "")
    cough = data.get("cough", "")
    breath = data.get("breath", "")

    # =========================
    # التشخيص الطبي
    # =========================

    # كوفيد-19
    if fever == "yes" and cough == "yes" and breath == "yes":

        result = "كوفيد-19"

        advice = """
الراحة، شرب السوائل بكثرة، ومراقبة الأعراض.
يفضل تجنب مخالطة الآخرين حتى التحسن.
راجع الطبيب إذا ظهرت صعوبة شديدة في التنفس أو ارتفاع مستمر في الحرارة.
"""

    # الإنفلونزا
    elif fever == "yes" and cough == "yes" and breath == "no":

        result = "الإنفلونزا"

        advice = """
الحصول على قسط كافٍ من الراحة.
شرب السوائل الدافئة بكثرة.
يمكن استخدام خافضات الحرارة عند الحاجة.
راجع الطبيب إذا استمرت الأعراض أو ازدادت.
"""

    # الزكام العادي
    elif cough == "yes" and fever == "no":

        result = "الزكام العادي"

        advice = """
الراحة وشرب السوائل الدافئة.
عادة تتحسن الأعراض خلال أيام قليلة.
راجع الطبيب إذا استمرت الأعراض.
"""

    # غير معروف
    else:

        result = "التشخيص غير معروف"

        advice = """
يرجى مراجعة الطبيب لإجراء تقييم طبي أدق.
"""

    return jsonify({
        "result": result,
        "advice": advice
    })


# =========================
# تشغيل السيرفر
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)