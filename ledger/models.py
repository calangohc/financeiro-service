from django.db import models

# Create your models here.
class Ledger(models.Model):
    ESCOLHAS = (
        ("Paypal", "paypal"),
        ("Caixa", "caixa"),
        ("Mercado pago", "mercado_pago")
    )
    data = models.DateField()
    quem = models.CharField(max_length=30)
    origem = models.CharField(max_length=20,choices=ESCOLHAS)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quem} doou {self.valor} via {self.origem}"
