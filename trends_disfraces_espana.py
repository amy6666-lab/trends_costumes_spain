from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

carpeta = Path(
    r"C:\Users\ameli\Documents\python\disfraces\analisis-trends-espana"
)

archivos_csv = list((carpeta / "data").rglob("time_series_*.csv"))

if not archivos_csv:
    raise FileNotFoundError("No se ha encontrado ningun archivo CSV")

archivo_csv = archivos_csv[0]
df = pd.read_csv(archivo_csv)

df["Time"] = pd.to_datetime(df["Time"])
df = df.sort_values("Time")
df["Año"] = df["Time"].dt.year
df["Mes_numero"] = df["Time"].dt.month

nombres_meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

plt.figure(figsize=(10, 4))
plt.plot(df["Time"], df["disfraces"], marker="o")

plt.title("Interes de busqueda por 'disfraces' en España")
plt.xlabel("Fecha")
plt.ylabel("Indice de interes (0-100)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

indice_maximos = df.groupby("Año")["disfraces"].idxmax()
picos = df.loc[indice_maximos, ["Time", "disfraces"]]

print("Mes con mayor interes de cada año:")
print(picos.to_string(index=False))

interes_medio_mes = (
    df.groupby("Mes_numero")["disfraces"]
    .mean()
    .sort_values(ascending=False)
)

interes_medio_mes.index = interes_medio_mes.index.map(nombres_meses)

print("Interes medio por mes del año:")
print(interes_medio_mes.round(2))

interes_medio_mes.sort_values().plot(
    kind="barh",
    figsize=(10, 6),
    title="Interes medio por 'disfraces' segun el mes"
)

plt.xlabel("Indice medio de interes")
plt.ylabel("Mes")
plt.tight_layout()
plt.show()

tabla_comparativa = df.pivot_table(
    index="Mes_numero",
    columns="Año",
    values="disfraces",
    aggfunc="mean"
)

print("Comparacion del interes por mes y año:")
tabla_mostrar = tabla_comparativa.copy()
tabla_mostrar.index = tabla_mostrar.index.map(nombres_meses)
print(tabla_mostrar.round(1).to_string())

tabla_grafico = tabla_comparativa.copy()
tabla_grafico.index = tabla_grafico.index.map(nombres_meses)

tabla_grafico.plot(
    kind="line",
    marker="o",
    figsize=(12, 6)
)

plt.title("Comparacion del interes por 'disfraces' segun el año")
plt.xlabel("Mes")
plt.ylabel("Indice de interes (0-100)")
plt.xticks(range(12), list(nombres_meses.values()), rotation=45)
plt.grid(True, alpha=0.3)
plt.legend(title="Año")
plt.tight_layout()
plt.show()

interes_mensual = df.groupby("Mes_numero")["disfraces"].mean()
cambio_mensual = interes_mensual.diff()

analisis_mensual = pd.DataFrame({
    "Interes_medio": interes_mensual,
    "Cambio_respecto_mes_anterior": cambio_mensual
})

analisis_mensual.index = analisis_mensual.index.map(nombres_meses)

print("Evolucion mensual del interes:")
print(analisis_mensual.round(2).to_string())

cambios_anuales = tabla_comparativa.diff()
cambios_anuales.index = cambios_anuales.index.map(nombres_meses)

print("Cambio mensual por año:")
print(cambios_anuales.round(1).to_string())

cambio_halloween = cambios_anuales.loc[
    ["Agosto", "Septiembre", "Octubre"]
].mean(axis=1)

cambio_carnaval = cambios_anuales.loc["Febrero"].mean()

print("Resumen para planificar campañas")
print("Halloween: cambio medio por mes")
print(cambio_halloween.round(2))

print("Carnaval: cambio medio de enero a febrero")
print(round(cambio_carnaval, 2), "puntos")

fig, ax = plt.subplots(figsize=(13, 7))

cambios_anuales.plot(
    kind="line",
    marker="o",
    linewidth=2,
    ax=ax
)

ax.axvspan(0.5, 1.5, alpha=0.12, color="orange")
ax.axvspan(8.5, 9.5, alpha=0.12, color="purple")

ax.set_title(
    "Cambios mensuales del interes por 'disfraces' en España",
    fontsize=14
)
ax.set_xlabel("Mes")
ax.set_ylabel("Cambio respecto al mes anterior (puntos)")

ax.grid(True, alpha=0.3)
ax.legend(title="Año")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()