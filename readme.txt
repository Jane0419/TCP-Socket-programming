��������˵��
����
����һ������TCPЭ���client-server����
client�˷���ASCII�ļ����server�ˣ����͵Ŀ鳤���������Χ��[lmin, lmax]֮�䡣
server�˽���reverse���������ظ�client�ˣ�client�˻����������´�ӡ������
�����н������ֱ�������Initialization��agree��reverseRequest��reverseAnswer�Ľ�����
server���ܹ�ͬʱ����2��������client�˵�ͬʱ����


���л���
Python 3.8.10

����ѡ��
IP��ַ��ip
�˿ںţ�port
�ļ�λ�ã�path
�����Ƭ���ȣ�lmin
���Ƭ���ȣ�lmax

���з�ʽ
guest os�ϣ�
python3 reversetcpserver.py
host os�������з�ʽ�£�
python udpclient.py <server_ip> <server_port>
python3 reversetcpclient.py <ip> <port> <path> <lmin> <lmax>

ע������
��ȷ��reversetcpserver.py��reversetcpclient.py����֮ǰ�Ѿ�����������reversetcpserver.py��ip��ַ�Ͷ˿���reversetcpclient.p����һ�¡�
�ļ�λ��ӦΪ�ͻ��˱��ش��ڵ��ļ�·����
