import yt_dlp
import sys

def download_youtube_content(url, mode):
    """
    유튜브 콘텐츠를 다운로드하는 함수
    :param url: 유튜브 영상 URL
    :param mode: 'video' 또는 'audio'
    """
    
    # 공통 옵션 설정
    ydl_opts = {
        # 파일 저장 이름 형식 (제목.확장자)
        'outtmpl': '%(title)s.%(ext)s',
        # 다운로드 중 에러 무시하지 않음
        'ignoreerrors': False,
        # 플레이리스트 다운로드 방지 (단일 영상만)
        'noplaylist': True,
    }

    if mode == 'audio':
        # 오디오 전용 옵션 (MP3 변환)
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
        print(f"🎵 오디오(MP3) 다운로드를 준비합니다: {url}")

    elif mode == 'video':
        # 비디오 전용 옵션 (최고 화질 비디오 + 최고 화질 오디오 병합)
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',  # 최종 결과물을 mp4로 병합
        })
        print(f"🎬 비디오(MP4) 다운로드를 준비합니다: {url}")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ 다운로드가 성공적으로 완료되었습니다!")
        
    except Exception as e:
        print(f"\n❌ 오류가 발생했습니다: {e}")

def main():
    print("=== 유튜브 다운로더 (yt-dlp 기반) ===")
    
    while True:
        url = input("\n유튜브 URL을 입력하세요 (종료하려면 q 입력): ").strip()
        
        if url.lower() == 'q':
            print("프로그램을 종료합니다.")
            break
            
        if not url:
            print("URL을 입력해주세요.")
            continue

        print("\n다운로드 형식을 선택하세요:")
        print("1. 비디오 (영상 + 소리)")
        print("2. 오디오 (MP3 소리만)")
        
        choice = input("선택 (1 또는 2): ").strip()

        if choice == '1':
            download_youtube_content(url, 'video')
        elif choice == '2':
            download_youtube_content(url, 'audio')
        else:
            print("잘못된 선택입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()
