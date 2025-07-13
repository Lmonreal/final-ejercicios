import module as final

def main():
    final.promedio_temperaturas('temperaturas.csv')
    final.count_words_per_line('content.txt')
    final.verificar_sesiones('users.txt', 'sessions.txt')
    final.gastos_por_categoria('gastos.txt')
    final.estadisticas_notas('notas.csv')

if __name__ == '__main__':
    main()