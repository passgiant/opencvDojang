import multiprocessing
import time

# 프로세스 함수 정의
def sum_numbers(start, end, queue):
    total = 0
    for i in range(start, end + 1):
        total += i
    queue.put(total)

if __name__ == '__main__':
    start_time = time.time()  # 시간 측정 시작

    # 멀티프로세싱 큐 생성
    queue = multiprocessing.Queue()

    # 프로세스 개수 설정
    num_processes = 4
    chunk_size = 100000000 // num_processes

    # 프로세스 리스트 생성
    processes = []

    # 프로세스 생성 및 시작
    for i in range(num_processes):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i < num_processes - 1 else 100000000
        process = multiprocessing.Process(target=sum_numbers, args=(start, end, queue))
        processes.append(process)
        process.start()

    # 모든 프로세스 완료 대기
    for process in processes:
        process.join()

    # 결과를 큐에서 가져와 합산
    total_sum = 0
    for _ in range(num_processes):  
        total_sum += queue.get()

    end_time = time.time()  # 시간 측정 종료
    print("1부터 100000000까지의 합:", total_sum)
    print("실행 시간: {:.2f} 초".format(end_time - start_time))