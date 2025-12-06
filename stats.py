import numpy as np
from scipy.stats import norm, t, chi2

#   ESTADÍSTICAS BÁSICAS
"""Funciones de la librerya numpy para calculos estadisticos basicos"""
def calcular_media(datos):
    return np.mean(datos)

def varianza_poblacional(datos):
    return np.var(datos)

def varianza_muestral(datos):
    return np.var(datos, ddof=1)

def desvio_poblacional(datos):
    return np.std(datos)

def desvio_muestral(datos):
    return np.std(datos, ddof=1)

#   COMPILAR TODAS LAS ESTADÍSTICAS

def calcular_estadisticas(datos):
    """Devuelve todas las estadísticas principales en un diccionario."""
    return {
        "Media": calcular_media(datos),
        "Varianza Poblacional": varianza_poblacional(datos),
        "Varianza Muestral": varianza_muestral(datos),
        "Desvío Poblacional": desvio_poblacional(datos),
        "Desvío Muestral": desvio_muestral(datos)
    }


#   INTERVALO DE CONFIANZA PARA LA MEDIA


def intervalo_media(datos, confianza):
    """Utiliza la normal si n es menor a 30 o en caso contrario la t de student de la libreria scipy"""
    n = len(datos)
    media = np.mean(datos)
    s = np.std(datos, ddof=1)
    alpha = 1 - confianza

    if n >= 30:
        z = norm.ppf(1 - alpha/2)
        margen = z * (s / np.sqrt(n))
    else:
        gl = n - 1
        t_crit = t.ppf(1 - alpha/2, df=gl)
        margen = t_crit * (s / np.sqrt(n))

    return (media - margen, media + margen)



#   INTERVALO DE CONFIANZA PARA LA VARIANZA
"""Calculo del intervalo de confianza para la varianza, calcula el limite inferior y superior
usando chi cuadrado de la libreria scipy """
def intervalo_varianza(datos, confianza):
    n = len(datos)
    gl = n - 1
    s2 = np.var(datos, ddof=1)
    alpha = 1 - confianza

    chi_der = chi2.ppf(1 - alpha/2, df=gl)
    chi_izq = chi2.ppf(alpha/2, df=gl)

    lim_inf = (gl * s2) / chi_der
    lim_sup = (gl * s2) / chi_izq

    return (lim_inf, lim_sup)
