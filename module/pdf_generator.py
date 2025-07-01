from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from markdown import markdown
from io import BytesIO

def generate_pdf(feedback_lines: list[str]) -> bytes:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        name="Title",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        fontSize=16,
        spaceAfter=20
    )

    story = [Paragraph("📄 CareerLens Résumé Feedback", title_style), Spacer(1, 12)]

    body_style = styles["Normal"]

    # Loop through lines and convert each to HTML paragraph
    for line in feedback_lines:
        line = line.strip()
        if line:
            html = markdown(line)  # line-by-line Markdown to HTML
            story.append(Paragraph(html, body_style))
            story.append(Spacer(1, 6))
        else:
            story.append(Spacer(1, 12))

    # Add watermark on all pages
    doc.build(story, onFirstPage=add_watermark, onLaterPages=add_watermark)
    return buffer.getvalue()

def add_watermark(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setFont("Helvetica", 40)
    canvas_obj.setFillColorRGB(0.9, 0.9, 0.9)
    canvas_obj.translate(300, 400)
    canvas_obj.rotate(45)
    canvas_obj.drawCentredString(0, 0, "CareerLens")
    canvas_obj.restoreState()