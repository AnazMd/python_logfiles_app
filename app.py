from flask import Flask, render_template, request
from log_summary import create_log_file, generate_summary, log_files


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        lines_per_log_file = int(request.form["lines"])

        # Create log files
        for log_file in log_files:
            create_log_file(log_file, lines_per_log_file)

        # Generate summary
        summary = generate_summary(log_files)
        totals = {
            "total_passed": sum(counts['pass'] for counts in summary.values()),
            "total_failed": sum(counts['fail'] for counts in summary.values()),
            "total_untested": sum(counts['untested'] for counts in summary.values())
        }

        print(totals)
        return render_template("index.html", summary=summary, totals=totals)
    else:
        return render_template("index.html", summary=None)


if __name__ == "__main__":
    app.run(debug=True)
